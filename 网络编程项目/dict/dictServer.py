# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/18 14:22
# @File_name:dictServer.py
# @IDE:PyCharm

"""
项目：电子词典
模块：socket，pymysql
"""

import socket
import pymysql
import os
import sys
import time


# 搭建网络
def main():
    address = ('0.0.0.0', 8888)
    # 创建数据库连接对象
    db = pymysql.connect('localhost', 'root', '123456', 'dict', charset='utf8')

    # 创建TCP套接字
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定地址
    server.bind(address)
    # 监听
    server.listen(10)
    print('等待客户端连接...........')

    # 连接客户端
    while True:
        try:
            client, addr = server.accept()
            print('客户端', addr, '连接过来了')
        except KeyboardInterrupt:
            sys.exit('服务器关闭')
        except Exception as e:
            print(e)
            continue

        # 创建进程，子进程和客户端交互，父进程等待其他客户端连接
        pid = os.fork()
        # 子进程和客户端交互，
        if pid == 0:
            doRequest(client, db)
            sys.exit('客户端退出')
        # 父进程等待其他客户端连接
        else:
            continue


# 处理客户端请求的函数
def doRequest(client, db):
    while True:
        message = client.recv(1024).decode()
        msgList = message.split(' ')
        if msgList[0] == 'E':
            break
        elif msgList[0] == 'R':
            # 处理注册函数
            doRegister(client, db, msgList[1], msgList[2])
        elif msgList[0] == 'L':
            # 处理登录函数
            doLogin(client, db, msgList[1], msgList[2])
        elif msgList[0] == "Q":
            # 进行查询
            doQuery(client, db, msgList[1], msgList[2])
        elif msgList[0] == "H":
            doHistory(client, db, msgList[1])


# 处理注册函数
def doRegister(client, db, username, password):
    # 判断此用户是否已存在
    cursor = db.cursor()
    sel = 'select password from user where username=%s'
    # 查看查询结果是否为空
    cursor.execute(sel, [username])
    # r 结果为元组
    r = cursor.fetchall()
    if r:
        client.send("EXISTS".encode())
        return
    else:
        # 用户不存在，进行注册
        ins = 'insert into user(username, password) values (%s, %s)'
        try:
            cursor.execute(ins, [username, password])
            db.commit()
            client.send("OK".encode())
        except Exception as e:
            db.rollback()
            client.send('FAIL'.encode())


# 处理登录函数
def doLogin(client, db, username, password):
    # 判断此用户是否已存在
    cursor = db.cursor()
    sel = 'select password from user where username=%s'
    # 查看查询结果是否为空
    cursor.execute(sel, [username])
    # r 结果为元组
    r = cursor.fetchall()
    if not r:
        client.send('NAMEERROR'.encode())
    elif r[0][0] == password:
        client.send('OK'.encode())
    else:
        client.send('PWDERROR'.encode())


# 查询单词
def doQuery(client, db, username, word):
    cursor = db.cursor()
    sel = 'select interpretation from words where word=%s'
    cursor.execute(sel, [word])
    # 获取查询结果
    result = cursor.fetchall()
    if not result:
        client.send(b"FAIL")
    else:
        client.send(result[0][0].encode())
        # 添加查询记录
        doInsHistory(cursor, username, word)
        db.commit()
        db.rollback()


# 添加历史记录
def doInsHistory(cursor, username, word):
    ins = 'insert into history(username, word, time) values(%s, %s, %s)'
    Time = time.ctime()
    try:
        cursor.execute(ins, [username, word, Time])
    except Exception as e:
        print(e)


# 查询历史记录
def doHistory(client, db, username):
    sel = 'select * from history where username=%s'
    cursor = db.cursor()
    cursor.execute(sel, [username])
    db.commit()
    result = cursor.fetchall()
    if not result:
        client.send(b'FAIL')
    else:
        client.send(b'OK')
        # 防止粘包
        time.sleep(0.1)

    for r in result:
        message = '%s %s %s' % (r[1], r[2], r[3])
        client.send(message.encode())

    client.send(b"##")


if __name__ == '__main__':
    main()
