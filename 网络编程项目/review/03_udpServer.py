# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/17 9:54
# @File_name:03_udpServer.py
# @IDE:PyCharm

import socket

# 创建套接字
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 设置复用
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定
server.bind(('0.0.0.0',8888))
print('正在等待客户端连接..........')
# 收发消息
while True:
    data, addr = server.recvfrom(1024)
    if not data:
        break
    print(addr, '对服务器说：', data.decode())
    server.sendto('服务器收到'.encode(), addr)

server.close()
