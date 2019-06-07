# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/13 17:02
# @File_name:demo08_stack_split.py
# @IDE:PyCharm

"""
多维数组的组合与拆分
"""

import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)

# 垂直方向的组合与拆分
c = np.vstack((a, b))
print(c)
a, b = np.vsplit(c, 2)
print(a, b, sep='\n')

# 水平方向的组合与拆分
d = np.hstack((a,b))
print(d)
a, b = np.hsplit(d,2)
print(a, b, sep='\n')

# 深度方向的组合与拆分
print('#'*50)
e= np.dstack((a,b))    # 笛卡尔坐标进行组合拆分
print(e)
a, b = np.dsplit(e,2)
print(a, b, sep='\n')

# 一维数组的组合方案
a = a.ravel()
b = b.ravel()
# 把a与b两个一维数组摞在一起成两行,  行并
c = np.row_stack((a, b))
# 把a与b两个一维数组组合在一起成两列，列并
d = np.column_stack((a, b))
print(c, d, sep='\n')

# 长度不等的数组的组合
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9])
# 把b补成5个元素, 头部补0个，尾部补1个，
# 新增元素的默认值为-1，头尾插入元素
b = np.pad(b, pad_width=(3, 1), mode='constant',constant_values=-1)
print(b)

