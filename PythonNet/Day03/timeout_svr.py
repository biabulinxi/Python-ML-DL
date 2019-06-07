# @Project:AID1810
# @Author:biabu
# @Date:18-12-6 下午4:51
# @File_name:timeout_svr.py
# @IDE:PyCharm

# 超时示例
import socket
import time

###创建scoket: socket
server = socket.socket()

###绑定地址　bind()
address = ("0.0.0.0",9999)
server.bind(address)

###监听 listen()
server.listen(10)
print('服务器已启动',address)

###接受请求 accept()
sockfd,addr = server.accept()       #阻塞
print("收到客户端请求",addr)

#循环接收
while True:
    ###数据接收 recv()
    data = sockfd.recv(1024)        #阻塞
    if not data:
        break
    print(data.decode())
#    time.sleep(10)
    sockfd.send("Timeout test msg".encode())

###关闭连接
sockfd.close()   #关闭通信socket
server.close()   #关闭监听socket
print("服务器已关闭")

