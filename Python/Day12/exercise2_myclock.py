# @Project:AID1810
# @Author:biabu
# @Date:2018/11/17 16:19
# @File_name:exercise2_myclock.py
# @IDE:PyCharm

#!usr\bin\python.exe

from time import *

while True:
    print(localtime()[3],':',localtime()[4],':',localtime()[5],sep='',end='\r')
    sleep(1)


