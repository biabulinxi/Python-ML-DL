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
    # 命令行输入IP地址和端口号
    if len(sys.argv) < 3:
        print('参数错误')
        return
    ADDRESS = (sys.argv[1], int(sys.argv[2]))

    # 创建UDP套接字
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 接收用户输入，包装后发送给服务端
    while True:
        name = input('请输入姓名：')
        message = 'L ' + name
        # 向服务器发送新消息
        client.sendto(message.encode(), ADDRESS)
        # 接受服务器反馈
        data, addr = client.recvfrom(1024)
        if data.decode() == "ok":
            print('您已进入聊天室')
            break
        else:
            # 打印不允许进入的原因
            print(data.decode())

    # 创建进程, 子进程发消息，父进程接收消息
    pid = os.fork()
    if pid < 0:
        sys.exit('创建进程失败')
    elif pid == 0:
        # 子进程发消息
        sendMsg(client, name, ADDRESS)
    else:
        # 父进程收消息
        recvMsg(client)


def sendMsg(client, name, ADDRESS):
    """子进程发送消息"""
    # 发消息给服务端，服务端在进行转发
    while True:
        content = input('请bb:')
        # 退出聊天室
        if content == 'quit':
            message = 'Q ' + name
            client.sendto(message.encode(), ADDRESS)
            sys.exit("已退出聊天室")
        # 包装信息

        message = 'C %s %s' % (name, content)
        client.sendto(message.encode(), ADDRESS)


def recvMsg(client):
    """父进程接收消息"""
    while True:
        message, addr = client.recvfrom(1024)
        # 父进程退出
        if message.decode() == 'exit':
            os._exit(0)
        print(message.decode()+'\n请发言(quit退出)',end='')


if __name__ == '__main__':
    main()
