# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/17 11:42
# @File_name:07_forkClient.py
# @IDE:PyCharm
"""多进程TCP并发客户点实现"""

import socket
import os
import sys

# 创建套接字
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 用户输入，获取命令行参数
if len(sys.argv) < 3:
    sys.exit('参数错误')
HOST = sys.argv[1]
PORT = int(sys.argv[2])
address = (HOST, PORT)

# 连接服务端
client.connect(address)
# 收发消息
while True:
    content = input("你想说：")
    client.send(content.encode())
    if not content:
        break
    data = client.recv(1024)
    print("服务器说：", data.decode())

# 关闭
client.close()












