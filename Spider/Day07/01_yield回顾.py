# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/6 9:48
# @File_name:01_yield回顾.py
# @IDE:PyCharm

def f1():
    print('启动生成器')
    for i in range(2):
        yield i
    print("*" * 30)

g = f1()
print(next(g))
print(next(g))
