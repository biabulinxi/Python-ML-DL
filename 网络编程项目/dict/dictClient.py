# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/18 14:22
# @File_name:dictClient.py
# @IDE:PyCharm

"""
项目：电子词典
模块：socket，pymysql
"""

import socket
import sys
import string
import getpass
from hashlib import sha1


# 搭建网络
def main():
    # 获取命令行参数
    if len(sys.argv) < 3:
        print('参数错误')
        return
    address = (sys.argv[1], int(sys.argv[2]))
    # 创建客户端
    client = socket.socket()
    try:
        # 连接服务器
        client.connect(address)
    except Exception as e:
        print(e)
        return

    # 客户端连接成功，进入下一级界面
    while True:
        prompt = '''
        *****************一级界面*****************
        --------1.注册   2.登录    3.退出---------
        *****************************************
        请选择(1/2/3):
        '''
        cmd = input(prompt)
        if cmd.isdigit() and cmd in ['1', '2', '3']:
            if cmd == "1":
                # 注册函数
                doRegister(client)
            elif cmd == '2':
                # 登录函数
                doLogin(client)
            else:
                # 退出函数
                doExit(client)
        else:
            print('输入有误，请输入(1/2/3)')


# 注册函数
def doRegister(client):
    # 所有字符
    allchars = string.punctuation + string.whitespace
    while True:
        username = input('\033[31m请输入注册的用户名：\033[0m')
        for u in username:
            if u in allchars:
                print("您输入的含有非法字符")
                break
        else:
            # 输入密码
            password1 = getpass.getpass('\033[31m请输入密码：\033[0m')
            password2 = getpass.getpass('\033[31m请再次输入密码：\033[0m')
            # 判断两次密码是否一致：
            if password1 == password2:
                # 创建加密对象
                s = sha1()
                s.update(password1.encode())
                password = s.hexdigest()
            else:
                print('两次密码不一致')
                continue
            # 向服务器发送用户信息
            message = 'R %s %s' % (username, password)
            client.send(message.encode())
            # 等服务器反馈
            data = client.recv(1024).decode()
            if data == 'OK':
                print('注册成功')
            elif data == 'EXISTS':
                print('该用户已存在')
            else:
                print('注册失败')

        # 直接跳转到一级界面
        return


# 登录函数
def doLogin(client):
    username = input('请输入用户名')
    password = getpass.getpass('请输入密码：')
    # 给密码加密
    s = sha1()
    s.update(password.encode())
    password = s.hexdigest()
    # 包装消息
    message = "L %s %s" % (username, password)
    client.send(message.encode())
    # 接收反馈结果
    data = client.recv(1024).decode()
    if data == "OK":
        print('登录成功')
        # 二级子界面
        doTwoLogin(client, username)
    elif data == 'NAMEERROR':
        print('用户名错误')
    else:
        print('密码错误')


# 退出一级子界面的函数
def doExit(client):
    client.send("E".encode())
    sys.exit(0)


# 二级子界面
def doTwoLogin(client, username):
    while True:
        prompt = """
                \033[32m
                ==================二级子界面=================
                --------1.查词   2.历史记录   3.注销----------
                请选择(1/2/3):\033[0m
                """
        cmd = input(prompt)
        if cmd not in ['1', '2', '3']:
            print("请正确选择")
        elif cmd == "1":
            # 查词函数
            doQuery(client, username)
        elif cmd == '2':
            # 查询历史记录
            doHistory(client, username)
        else:
            # 终止死循环， 自动跳转到一级界面，嵌套循环
            break


# 查词函数
def doQuery(client, username):
    while True:
        word = input("请输入要查询的单词(##退出):")
        if word == "##":
            break
        # 包装消息
        message = "Q %s %s" % (username, word)
        client.send(message.encode())
        data = client.recv(1024).decode()
        if data == "FAIL":
            print('词库中没有该单词')
        else:
            print(data)


# 查询历史记录
def doHistory(client, username):
    message = "H %s" % username
    client.send(message.encode())
    data = client.recv(1024).decode()
    if data == "OK":
        while True:

            if data == "##":
                break
            print(data)
    print("没有历史记录")


if __name__ == '__main__':
    main()
