# @Project:AID1810
# @Author:biabu
# @Date:18-11-21 上午10:16
# @File_name:myinteger.py
# @IDE:PyCharm


def myinteger(n):
    i = 0
    while i < n:
        yield i
        i += 1
for x in myinteger(3):
    print(x)