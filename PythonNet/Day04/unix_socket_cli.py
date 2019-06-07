# @Project:AID1810
# @Author:biabu
# @Date:18-12-11 上午11:35
# @File_name:unix_socket_cli.py
# @IDE:PyCharm

from socket import *
sock_file = "sock_file"

client = socket(AF_UNIX,SOCK_STREAM)
client.connect(sock_file)

while True:
    msg = input("请输入发送的信息：")
    if not msg:
        continue
    if msg == "q" or msg =="Q":
        break
    else:
        client.send(msg.encode())

client.close()
