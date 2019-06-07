# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/17 9:38
# @File_name:ftpClient.py
# @IDE:PyCharm

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1', 8888)
client.connect(address)
# 发消息
content = input('你想说：')
client.send(content.encode())
# 收消息
data = client.recv(1024)
print(data.decode())
# 关闭
client.close()
