# @Project:AID1810
# @Author:biabu
# @Date:2018/11/14 17:48
# @File_name:exercise2_myfac.py
# @IDE:PyCharm

def myfac(n):
    fac = 1
    for i in range(1,n + 1):
        fac *= i
    return fac

print(myfac(5))  # 120