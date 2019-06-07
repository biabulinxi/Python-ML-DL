# @Project:AID1810
# @Author:biabu
# @Date:18-12-11 下午2:27
# @File_name:struct_svr.py
# @IDE:PyCharm

from socket import *

import struct

address = ('0.0.0.0',9999)
server = socket(AF_INET, SOCK_DGRAM)
server.bind(address)

while True:
    # 接收fmt格式字符串
    data,addr = server.recvfrom(1024)
    fmt = data.decode()
    print(fmt)

    # 调用struct.unpack()接收数据
    data, addr = server.recvfrom(1024)
    msg = struct.unpack(fmt, data)
    print(msg)

server.close()