# @Project:AID1810
# @Author:biabu
# @Date:18-12-10 上午11:25
# @File_name:simple_select.py
# @IDE:PyCharm

# select函数

from socket import *
import select

server = socket()
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

server.bind(('0.0.0.0',9999))
server.listen(5)
print('服务器已启动')

# 定义三个列表
rlist = [server]  # 用来记录IO读操作
wlist = []  # 用来记录IO写操作
xlist = []  # 用来记录IO异常操作

# 调用select，当IO事件要进行时，进行选择返回
while True:
    rs, ws, xs = select.select(rlist, wlist, xlist)
    print("监控到IO事件发生")

    # 返回遍历IO列表，依次进行处理
    for r in rs:  # 读事件就绪IO列表，读数据
        if r is server:    # 就绪IO是监听socket
            client, addr = server.accept()  # 允许连接
            print('New connect from:', addr)
            # 将与客户端通信的IO的读事件放入读列表
            rlist.append(client)
        else:              # 就绪IO是数据传输socket
            data = r.recv(1024)
            if not data:
                rlist.remove(r)   # 移除，不在关注
                continue
            else:
                print('收到的数据：',data.decode())
                wlist.append(r)
    for w in ws:  # 写事件列表，写数据
        w.send(b'Test Msg')
        wlist.remove(w)

    for x in xs:  # 异常处理
        pass



server.close()
