# @Project:AID1810
# @Author:biabu
# @Date:18-12-7 下午4:18
# @File_name:class_exercise_send.py
# @IDE:PyCharm


'''读取图片文件发送到服务端，读取完毕，程序退出'''

from socket import *

# 创建套接字
s = socket(AF_INET,SOCK_DGRAM)
address = ("127.0.0.1",9999)

# 发送文件
with open("th.jpg",'rb') as image:
    # 循环读取
    while True:
        data = image.read(1024)
        if not data:
            break
        s.sendto(data,address)
    print("文件已发送")

# 关闭连接
s.close()
