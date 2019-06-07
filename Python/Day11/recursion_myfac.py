# @Project:AID1810
# @Author:biabu
# @Date:2018/11/15 14:55
# @File_name:recursion_myfac.py
# @IDE:PyCharm

'''函数求阶乘
def myfac(n):
    fac = 1
    for i in range(1,n + 1):
        fac *= i
    return fac

print(myfac(5))  # 120
'''


# 递归求阶乘
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))    #120

