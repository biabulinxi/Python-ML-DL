# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/17 14:48
# @File_name:qqServer.py
# @IDE:PyCharm

"""
名称：网络聊天室
环境：python3.5
技术：socket fork
"""

import socket
import os
import sys


# 创建网络连接
def main():
    # 创建UDP套接字
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 设置端口复用
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定地址
    ADDRESS = ("0.0.0.0", 8888)
    server.bind(ADDRESS)

    # 创建多进程，子进程负责管理员喊话，父进程和客户端交互
    pid = os.fork()
    if pid < 0:
        # 一旦进程创建失败，就结束
        print("进程创建失败")
        return
    elif pid == 0:
        print('负责管理员喊话的进程')
        while True:
            content = input('管理员消息')
            # 包装消息
            message = 'C 管理员 %s' % content
            # 父进程监听， 发送消息给父进程
            server.sendto(message.encode(),ADDRESS)

    else:
        # 父进程处理客户端的各种请求
        doRequest(server)


# 处理客户端请求的函数
def doRequest(server):
    # 定义用户存储结构
    user = {}

    while True:
        # 收消息
        message, addr = server.recvfrom(1024)
        # msgList：['L','金毛狮王']
        msgList = message.decode().split()
        if msgList[0] == 'L':
            doLogin(server, user, msgList[1], addr)
        elif msgList[0] == 'C':
            content = ' '.join(msgList[2:])
            # 发送给其他人
            doChat(server, content, user, msgList[1])
        elif msgList[0] == 'Q':
            doQuit(server, msgList[1], user)


def doLogin(server, user, name, addr):
    """
    进入聊天室的请求处理函数
    server:服务端
    user：用户字典{name:addr}
    """
    # 判断姓名是否存在
    if (name in user) or name == '管理员':
        server.sendto('该用户已经存在'.encode(), addr)
        return
    # 名字不存在，发送OK客户端，允许进入
    server.sendto('ok'.encode(), addr)
    # 通知其他人有人进来了
    message = '\n欢迎%s进入聊天室' % name
    for u in user:
        server.sendto(message.encode(), user[u])
    # 加入存储结构user中
    user[name] = addr


def doChat(server, content, user, name):
    """发消息发送给其他成员"""
    # 丰满消息
    message = '\n %s说:%s' % (name, content)
    for u in user:
        # 发给其他成员
        if u != name:
            server.sendto(message.encode(), user[u])


def doQuit(server, name, user):
    """客户端退出函数"""
    # 通知其他成员
    message = '\n %s 退出了聊天室' % (name)
    for u in user:
        if u != name:
            server.sendto(message.encode(), user[u])
        else:
            # 给退出者发送允许退出
            server.sendto(b"exit")
    # 删除退出者
    del user[name]


if __name__ == '__main__':
    main()
