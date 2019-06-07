# @Project:AID1810
# @Author:biabu
# @Date:2018/11/15 18:16
# @File_name:exercise2_list_sum.py
# @IDE:PyCharm


L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]

def print_list(lst):
    for i in lst:
        if type(i) is int:
            print(i)
        elif type(i) is list:   # 不能 return 函数递归
            print_list(i)

def sum_list(lst):
    sum1 = 0
    for i in lst:
        if type(i) is int:
            sum1 += i
        elif type(i) is list:
            sum1 += sum_list(i)
    return sum1

print(print_list(L))

print(sum_list(L))

a
16
100
b
15
88
c
18
99
