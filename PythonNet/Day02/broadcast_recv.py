# @Project:AID1810
# @Author:biabu
# @Date:18-12-7 下午3:54
# @File_name:broadcast_recv.py
# @IDE:PyCharm

from socket import *

#　创建

s = socket(AF_INET,SOCK_DGRAM)

# 设置接收
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",9999))

#接收
while True:
    try:
        msg, addr = s.recvfrom(1024)
        print("收到来自%s信息的%s" % (addr,msg.decode()))
    except:
        print("接受异常")
        break

#关闭
s.close()