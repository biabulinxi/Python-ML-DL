# @Project:AID1810
# @Author:biabu
# @Date:2018/11/15 15:02
# @File_name:recursion_mysum.py
# @IDE:PyCharm


def recursion_mysum(n):
    if n == 1:
        return 1
    return n + recursion_mysum(n - 1)

print(recursion_mysum(100))