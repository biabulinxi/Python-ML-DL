# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/21 11:04
# @File_name:ftpServer.py
# @IDE:PyCharm

# 1. 创建套接字，绑定，监听
# 2. 接收客户端连接
# 3. 创建新的线程，处理客户端请求
# 4. 主线程继续等待其他客户端连接
# 5.当客户端退出时处理对应线程

from socket import *
from threading import Thread
import sys


# 主线程处理客户端函数
def handler(client):
    while True:
        message = client.recv(1024)
        if not message:
            break
        print(message.decode())
        client.send('服务端收到'.encode())


address = ("0.0.0.0",8888)
# 创建绑定监听
server = socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(address)
server.listen(10)

print("正在等待客户端连接..........")

while True:
    try:
        client, addr = server.accept()
    except KeyboardInterrupt:
        sys.exit('服务器退出')
    except Exception as e:
        print(e)
        continue

    # 连接成功，创建线程
    t = Thread(target=handler, args=(client,))
    # 设置守护线程，主线程结束后，子线程也随之退出，主线程为服务器
    t.setDaemon(True)
    t.start()




















