# @Project:AID1810
# @Author:biabu
# @Date:18-12-11 上午11:26
# @File_name:unix_socket_server.py
# @IDE:PyCharm

# 本地套接字示例

from socket import *
import os

# 创建套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)
# 套接字文件
sock_file = "sock_file"
# 若存在，则删除套接字文件
if os.path.exists(sock_file):
    os.remove(sock_file)
# 绑定地址，并创建套接字文件
sockfd.bind(sock_file)
# 监听
sockfd.listen(3)
# 允许连接
while True:
    client,addr = sockfd.accept()
    # 接收数据
    while True:
        data = client.recv(1024)
        print(data.decode())

sockfd.close
