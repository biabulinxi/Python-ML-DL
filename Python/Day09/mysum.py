# @Project:AID1810
# @Author:biabu
# @Date:2018/11/13 11:55
# @File_name:mysum.py
# @IDE:PyCharm

def mysum(*args):
    sum1 = 0
    for i in args:
        sum1 += i
    return sum1


print(mysum())  # 0
print(mysum(1,2,3,4))  # 10