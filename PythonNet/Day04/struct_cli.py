# @Project:AID1810
# @Author:biabu
# @Date:18-12-11 下午2:17
# @File_name:struct_cli.py
# @IDE:PyCharm

from socket import *
import struct

address = ("127.0.0.1",9999)
client = socket(AF_INET,SOCK_DGRAM)

while True:
    id = int(input("id:"))
    name = input("name:")
    n = len(name)
    height = float(input("height:"))

    fmt = 'i%dsf' % n
    # 按照格式转换字节序列
    data = struct.pack(fmt,id,name.encode(),height)
    # 发送格式
    client.sendto(fmt.encode(), address)
    # 发送数据
    client.sendto(data, address)

client.close()