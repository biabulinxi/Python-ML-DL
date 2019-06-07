# @Project:AID1810
# @Author:biabu
# @Date:18-12-7 上午11:48
# @File_name:UDP_cli.py
# @IDE:PyCharm

from socket import *
address = ("127.0.0.1", 9999)

#创建
client = socket(AF_INET,SOCK_DGRAM)

#收发数据
while True:
    data = input("请输入要发送的信息：")
    if not data:
        continue
    if data == "q" or data == "Q":
        break
    #发送数据
    client.sendto(data.encode(),address)

    #接收数据
    resp, addr = client.recvfrom(1024)
    if resp:
        print(resp.decode())

#关闭
client.close()



