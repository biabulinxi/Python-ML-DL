# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/13 11:01
# @File_name:demo02_ndarry.py
# @IDE:PyCharm

"""
ndarray 的常用方法
"""

import numpy as np

# 创建二维数组
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a, a.shape)

# 起始值1，终止值10，不长2
b = np.arange(1, 10, 2)
print(b)

# 创建10个元素全为0的数组
c = np.zeros(10, dtype='bool')
print(c,c.dtype)

# 创建10个元素全为1的数组
d = np.ones(10, dtype='int32')
print(d,d.dtype)

# 创建与a数组结构相同的0,1数组
e = np.zeros_like(a)
f = np.ones_like(a)
print(e)
print(f)
