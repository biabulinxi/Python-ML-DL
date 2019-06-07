# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/20 10:55
# @File_name:demo03_vectorize.py
# @IDE:PyCharm

"""
函数矢量化
"""

import numpy as np
import math


def func(a, b):
    r = math.sqrt(a**2 + b**2)  # np.sqrt 默认是矢量运算
    return r

print(func(3, 4))
a = np.array([3,4,5])
b = np.array([4,5,6])

# 函数矢量化
f_vec = np.vectorize(func)
print(f_vec(a,b))

# 使用frompyfunc实现函数矢量化
# 2： 函数有两个参数，  1：函数有一个返回值
f_func = np.frompyfunc(func, 2, 1)
print(f_func(a,b))