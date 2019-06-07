# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/21 11:04
# @File_name:ftpServer.py
# @IDE:PyCharm

# 1. 创建套接字，绑定，监听
# 2. 接收客户端连接
# 3. 创建新的线程，处理客户端请求
# 4. 主线程继续等待其他客户端连接
# 5.当客户端退出时处理对应线程

from socket import *
from threading import Thread
import sys
import os
import time

# 定义全局变量
address = ("0.0.0.0", 8888)
# fileDir = 'C:/Users/Pycharm/AID1810/网络编程项目/FTP_file_server/tcpFile/'
fileDir = './tcpFile/'
get_fileDir = './tcpFile/get/'


# 主线程处理客户端函数
def doRequest(client):
    # 接收客户端的各种请求
    while True:
        # 创建对象，每个客户端都有单独的对象
        serverObj = FtpServer(client)
        # 接收客户端包装好的请求
        message = client.recv(1024).decode()
        msgList = message.split(" ")
        if msgList[0] == "L":
            serverObj.doList()
        elif msgList[0] == "G":
            serverObj.doGet(msgList[-1])
        elif msgList[0] == "P":
            serverObj.doPut(msgList[-1])
        elif msgList[0] == "Q":
            serverObj.doExit()


# 具体功能实现类
class FtpServer(object):
    def __init__(self, client):
        self.client = client

    # 显示文件列表
    def doList(self):
        # 利用os.listdit() 把内容放到列表
        fileList = os.listdir(fileDir)
        if not fileList:
            self.client.send("文件库为空".encode())
        else:
            self.client.send(b"OK")
            # 防止粘包
            time.sleep(0.1)

        # 发送文件名到客户端
        for file in fileList:
            # 判断是否为普通文件
            if os.path.isfile(fileDir + file) and file[0] != '.':
                self.client.send(file.encode())
                # 防止粘包
                time.sleep(0.1)
        # 发送 ## 表示结束
        self.client.send(b"##")

    # 下载文件
    def doGet(self, filename):
        # 判断文件是否存在
        try:
            f = open(fileDir + filename, "rb")
        except:
            self.client.send("文件不存在".encode())
            return
        # 文件正常打开
        self.client.send(b'OK')
        time.sleep(0.1)
        # 发送文件内容
        while True:
            data = f.read(1024)
            if not data:
                # 处理粘包
                time.sleep(0.1)
                self.client.send(b"##")
                break
            else:
                self.client.send(data)
        f.close()

    # 上传文件
    def doPut(self, filename):
        try:
            f = open(fileDir + filename, "wb")
        except:
            self.client.send("上传失败".encode())
            return
        self.client.send(b"OK")
        # 接收
        while True:
            data = self.client.recv(1024)
            if data == b"##":
                break
            f.write(data)
        f.close()

    # 退出系统
    def doExit(self):
        sys.exit(0)


# 创建网络连接
if __name__ == '__main__':

    # 创建绑定监听
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(address)
    server.listen(10)

    print("正在等待客户端连接..........")

    while True:
        try:
            client, addr = server.accept()
        except KeyboardInterrupt:
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue

        # 连接成功，创建线程
        print("客户端连接成功")
        t = Thread(target=doRequest, args=(client,))
        # 设置守护线程，主线程结束后，子线程也随之退出，主线程为服务器
        t.setDaemon(True)
        t.start()
