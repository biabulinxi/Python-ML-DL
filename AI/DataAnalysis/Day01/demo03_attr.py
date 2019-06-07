# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/13 11:18
# @File_name:demo03_attr.py
# @IDE:PyCharm

"""
ndarry的属性
"""
import numpy as np

# 测试数组的维度
a = np.arange(1,10)
print(a, a.shape)
a.shape = (3,3)
print(a, a.shape)

# 测试元素的类型
print(a.dtype)
b = a.astype(float)
print(b, b.dtype)
b[0][0] = 999
print(b)
print(a)

# 测试元素个数，数组的大小
print('a.size:',a.size,'len(a):',len(a))

# 测试元素的索引下标
# 3页2行3列
c = np.arange(1,19).reshape(3,2,3)
print(c)
print(c[0]) # 第一页的数据
print(c[0][0]) # 第一页第一行的数据
print(c[0][0][0]) # 第一页第一行第一列的数据
print(c[0,0,0]) # 第一页第一行第一列的数据

# 遍历c中的每个元素并输出
for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[2]):
            print(c[i,j,k],end=' ')

