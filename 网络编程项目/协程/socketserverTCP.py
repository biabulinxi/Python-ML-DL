# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/21 18:35
# @File_name:socketserverTCP.py
# @IDE:PyCharm

from socketserver import *

# 创建服务类 TCP + 多进程
# python 支持多继承
class Server(ForkingMixIn, TCPServer):
    pass

# 创建处理请求类
class Handler(StreamRequestHandler):
    # 重写 handle 方法
    def handle(self):
        # client_address属性：客户端地址
        print(self.client_address,"连接过来了")
        while True:
            # self.request 属性：套接字
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send("服务器收到".encode())
            

# 创建服务器对象
server = Server(('0.0.0.0',8888),Handler)
# 启动
server.serve_forever()













