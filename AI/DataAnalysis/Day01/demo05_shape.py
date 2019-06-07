# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/13 15:31
# @File_name:demo05_shape.py
# @IDE:PyCharm

"""
数则维度操作
"""

import numpy as np

a = np.arange(1,9)
print(a,a.shape)
#########################################
# 视图变维
# a,b指向的原始数据，发生了改变，可知，b是a引用关系元数据的赋值改变，实际数据不变
b = a.reshape(2,4)
print(b, b.shape)
b[0,0] = 999
print(a)
print(b)
# 抻平元素
c = a.ravel()
print(c)

#########################################
# 复制变维度，实际数据的复制，数据独立
print("#"*50)
# 抻平元素
d = b.flatten()
d[2] = 777
print(b)
print(d)

#########################################
# 就地变维
print('#'*50)
b.shape = (4,2)
print(b)
b.resize(2,2,2)
print(b)
