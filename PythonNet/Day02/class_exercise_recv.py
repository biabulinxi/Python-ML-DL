# @Project:AID1810
# @Author:biabu
# @Date:18-12-7 下午4:32
# @File_name:class_exercise_recv.py
# @IDE:PyCharm

from socket import *


# 创建套接字
s = socket(AF_INET,SOCK_DGRAM)
address = ("0.0.0.0",9999)

# 绑定连接
s.bind(address)
print("服务器已启动")

# 接收数据
with open("recv.jpg",'wb') as image:
    # 循环读取
    while True:
        data, addr = s.recvfrom(1024)
        image.write(data)
        if not data:
            break
        print("已接收")

# 关闭连接
s.close()