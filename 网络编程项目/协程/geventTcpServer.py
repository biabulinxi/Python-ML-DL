# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/21 18:04
# @File_name:geventTcpServer.py
# @IDE:PyCharm

import gevent
from gevent import monkey
# 执行脚本，修改阻塞行为
monkey.patch_socket()

# 导入模块
from socket import *

# 创建套接字
def Server():
    # 默认为TCP
    server = socket()
    address = ('0.0.0.0',8888)
    server.bind(address)
    server.listen(10)
    print("等待连接........")
    while True:
        client, addr = server.accept()
        print(addr,"连接过来了")
        # 处理客户端的请求函数
        handle(client)
        # 使用协程，接收多个客户端连接,实现并发
        gevent.spawn(handle,client)

# 处理客户端求
def handle(client):
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        client.send('服务端收到'.encode())
        client.close()


if __name__ == '__main__':
    Server()
















