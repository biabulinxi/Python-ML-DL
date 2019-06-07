# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/8 8:58
# @File_name:01_abc.py
# @IDE:PyCharm

"""
引入
先来看一道题:
如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
"""

import time


def abc1():
    """
    枚举法
    基本运算数量：T = 1000 * 1000 * 1000 * 10
    时间复杂度：T(n) = n^3
    :return: None
    """
    start_time = time.time()
    # 注意是三重循环
    for a in range(0, 1001):
        for b in range(0, 1001):
            for c in range(0, 1001):
                if a**2 + b**2 == c**2 and a+b+c == 1000:
                    print("a, b, c: %d, %d, %d" % (a, b, c))
    end_time = time.time()
    print("elapsed: %f" % (end_time - start_time))
    print("complete!")


def abc2():
    """
    基本运算数量：T = 1000 * 1000  * 7
    时间复杂度：T(n) = n^2  大O记法

    T(n) = n * n * (1 + max(1,0))
         = n^2 * 2
         = n^2

    :return: None
    """
    start_time = time.time()
    # 注意是两重循环
    for a in range(0, 1001):
        for b in range(0, 1001 - a):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print("a, b, c: %d, %d, %d" % (a, b, c))
    end_time = time.time()
    print("elapsed: %f" % (end_time - start_time))
    print("complete!")


if __name__ == '__main__':

    # 顺序 : 加法
    # 条件(分支)  : 取最大值
    # 循环 : 乘法

    # abc1()
    abc2()

