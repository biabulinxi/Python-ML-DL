# @Project:AID1810
# @Author:biabu
# @Date:18-12-11 上午9:34
# @File_name:epoll.py
# @IDE:PyCharm

# @Project:AID1810
# @Author:biabu
# @Date:18-12-10 下午4:25
# @File_name:poll.py
# @IDE:PyCharm

from socket import *
from select import *

address = ("0.0.0.0",9999)

server = socket()
server.bind(address)
server.listen(5)
print('服务器已启动：',address)

p = epoll()   # create poll object
p.register(server.fileno(),EPOLLIN)  # register IO

fdmap = { # 字典：存放fd和socket映射对象
        server.fileno():server}
# 循环监控
while True:
    events = p.poll()    # 阻塞，等待IO事件
    print(events)
    for fd,e in events: # 循环处理
        sock = fdmap[fd]  # 通过fd取得scoket对象
        #　判断就绪IO是否为监听socket
        if fd == server.fileno():
            client,addr = server.accept()
            print("收到连接：",addr)
            # 注册事件
            # EPOLLIN | EPOLLET 表示标记叠加
            p.register(client, EPOLLIN | EPOLLET)
            # 将连接的socket放入映射表
            fdmap[client.fileno()] = client

        elif e & EPOLLIN: # 判断event是否可读
            data = sock.recv(1024)
            if not data:
                p.unregister(fd) # 从关注列表移除
                sock.close()     # 关闭连接
                del sock         # 释放对象
            else:
                print("收到数据：",data.decode())
                sock.send(b"test msg")





