# @Project:AID1810
# @Author:biabu
# @Date:2018/11/15 17:43
# @File_name:exercise1_fac_sum.py
# @IDE:PyCharm


def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)

def mysum(x):
    if x == 1:
        return 1
    return fac(x) + mysum(x - 1)

print(mysum(20))


