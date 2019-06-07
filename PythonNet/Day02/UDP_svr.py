# @Project:AID1810
# @Author:biabu
# @Date:18-12-7 上午11:37
# @File_name:UDP_svr.py
# @IDE:PyCharm

from socket import *
address = ("0.0.0.0",9999)

#创建
server = socket(AF_INET,SOCK_DGRAM)

#绑定
server.bind(address)
print("服务器已启动",address)

#收发消息
while True:
    data,addr = server.recvfrom(1024)
    if not data:
        break
    print("收到数据",data.decode())
    print("发送自：",addr)

    #回数据
    resp = input("请回复:")
    server.sendto(resp.encode(),addr)

# 关闭服务器
server.close()
