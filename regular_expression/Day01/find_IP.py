# @Project:AID1810
# @Author:biabu
# @Date:18-12-18 上午9:37
# @File_name:find_IP.py
# @IDE:PyCharm


"""
# 读取文件内容，得到一个列表
with open("access.log",'r') as f:
    lines = f.readlines()
    for line in lines:
        IP = line[0:13]
        print(IP)
"""

# 正则
import re

with open("access.log", 'r') as f:
    lines = f.read()
    IP = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\."
                    "\d{1,3}", lines)
    print(IP)

    macIP = re.findall("[0-9a-f]{2}:[0-9a-f]{2}:"
                       "[0-9a-f]{2}:[0-9a-f]{2}:"
                       "[0-9a-f]{2}:[0-9a-f]{2}", lines)

    print(macIP)
