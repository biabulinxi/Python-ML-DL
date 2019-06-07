# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/17 11:13
# @File_name:07_forkServer.py
# @IDE:PyCharm

'''多进程TCP并发实现'''
import socket
import os
import sys


# 创建套接字，绑定地址，监听
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
address = ('0.0.0.0',8888)
server.bind(address)
server.listen(5)


def clientHandle(client, addr):
    print('客户端',addr,'连接过来了')
    while True:
        data = client.recv(1024)
        if not data:
            break
        else:
            print(addr,'说：',data.decode())
            client.send('服务端收到'.encode())


# 等待客户端连接
print('正在等待客户端连接...........')
while True:
    try:
        client, addr = server.accept()
    except KeyboardInterrupt:
        sys.exit('服务器退出')
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        # 创建二级子进程和客户端交互
        pid = os.fork()
        if pid == 0:
            server.close()
            # 处理和客户端交互
            clientHandle(client,addr)
            os._exit(0)
        else:
            # 一级子进程退出
            os._exit(0)
    else:
        # 处理僵尸进程
        os.wait()
        # 继续等待其他客户端连接
        continue

















