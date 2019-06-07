# @Project:AID1810
# @Author:biabu
# @Date:18-12-7 下午3:42
# @File_name:broadcast_send.py
# @IDE:PyCharm


# IP:176.234.82.51
# 广播:176.234.82.255
# 掩码:255.255.255.0

from socket import *

# 设置广播地址
dest = ("176.234.82.255",9999)
s = socket(AF_INET, SOCK_DGRAM)  #创建UDP套接字

#设置广播选项
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

#发送信息
msg = "Broadcast test message"
s.sendto(msg.encode(),dest)
print("广播信息已发送")

#关闭
s.close()
