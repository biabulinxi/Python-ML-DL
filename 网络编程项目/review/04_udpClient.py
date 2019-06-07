# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/17 10:01
# @File_name:04_udpClient.py
# @IDE:PyCharm

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 收发消息
while True:
    content = input('你想说：')
    if not content:
        break
    address = ('127.0.0.1', 8888)
    client.sendto(content.encode(),address)
    data, addr = client.recvfrom(1024)
    print(data.decode())

client.close()
