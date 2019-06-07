# @Project:AID1810
# @Author:biabu
# @Date:18-12-6 下午5:04
# @File_name:timeout_cli.py
# @IDE:PyCharm
# 超时示例

import socket

address = ("127.0.0.1",9999)

# 创建scoket
client = socket.socket()

# 连接服务器 connect()
client.settimeout(5)  # 设置超时
client.connect(address)

#循环输入
while True:
    # 发送数据 send()
    msg = input("请输入要发送的信息：")
    # 输入Q退出
    if msg == "q" or msg == "Q":
        break
    client.send(msg.encode())
    print("消息已发送")

    data = client.recv(1024)
    print(data.decode())

# 关闭连接
client.close()
print("客户端已关闭")