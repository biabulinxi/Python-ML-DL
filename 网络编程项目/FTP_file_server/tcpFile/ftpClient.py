# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/17 9:38
# @File_name:ftpClient.py
# @IDE:PyCharm

from socket import *
import sys
import time


# 具体功能实现类
class FtpClient(object):
    def __init__(self,client):
        # 定义client为类内属性
        self.client = client

    # 文件列表
    def doList(self):
        # 向服务端发送请求
        self.client.send(b"L")
        # 接收
        data = self.client.recv(1024).decode()
        if data == "OK":
            while True:
                filename = self.client.recv(1024).decode()
                if filename == "##":
                    break
                # 打印接收的文件名
                print("\033[32m"+filename+"\033[0m")
        else:
            print(data)

    # 下载文件
    def doGet(self):
        filename = input("请输入要下载的文件名：")
        message = "G " + filename
        self.client.send(message.encode())
        # 接收服务端反馈
        data = self.client.recv(1024).decode()
        if data == "OK":
            # 打开本地文件
            f = open(filename, 'wb')
            while True:
                data = self.client.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()
            print('%s 下载完成' % filename)
        else:
            print(data)

    # 上传文件
    def doPut(self):
        filename = input("请输入要上传的文件：")
        # 按路径切割
        filename2 = filename.split("/")[-1]
        try:
            f = open(filename, 'rb')
        except:
            print("没有这个文件")
            return
        # 发送请求
        message = "P " + filename2
        self.client.send(message.encode())
        data = self.client.recv(1024).decode()
        if data == "OK":
            # 上传文件，发送数据
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.client.send(b"##")
                    break
                else:
                    self.client.send(data)
            f.close()
            print("%s 上传完成" % filename2)

    # 退出系统
    def doExit(self):
        self.client.send(b"Q")
        sys.exit("谢谢使用")


# 创建连接网络
if __name__ == '__main__':
    # if len(sys.argv) < 3:
    #     print("参数错误")
    # address = (sys.argv[1],int(sys.argv[2]))
    address = ("127.0.0.1",8888)

    # 创建套接字
    client = socket(AF_INET, SOCK_STREAM)
    try:
        client.connect(address)
    except Exception as e:
        print('连接服务器失败', e)
    # 连接成功，进入界面
    while True:
        # 创建对象，调用类方法
        clientObj = FtpClient(client)

        # 界面
        print("""\033[31m===========风云网盘=============
                 ******  1. 查看文件列表 ********
                 ******  2. 下载文件     ********
                 ******  3. 上传文件     ********
                 ******  4. 退出网盘     ********
                 ===============================\033[0m""")
        cmd = input("\033[31m请选择(1/2/3/4):\033[0m")
        # 做判断
        if cmd.strip() in ['1', '2', '3', '4']:
            if cmd == '1':
                # 显示文件列表
                clientObj.doList()
            elif cmd == '2':
                # 下载文件
                clientObj.doGet()
            elif cmd == '3':
                # 上传文件
                clientObj.doPut()
            elif cmd == '4':
                # 退出系统
                clientObj.doExit()
        else:
            print("请正确选择！")






















