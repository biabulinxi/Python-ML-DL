# @Project:AID1810
# @Author:biabu
# @Date:2018/11/15 15:28
# @File_name:recursion_age.py
# @IDE:PyCharm


def num(n):
    if n == 1:
        return 10
    return 2 + num(n - 1)

print(num(1))
print(num(2))
print(num(3))
print(num(4))
print(num(5))
