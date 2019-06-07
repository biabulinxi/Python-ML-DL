# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/7 13:28
# @File_name:numpy_attribute.py
# @IDE:PyCharm

import numpy as np

array = np.array([[1,2,3],[4,5,6]])

print(array)
# 获得矩阵的形状,
print(array.shape)  # (2, 3) 两行三列
# 获得矩阵元素的个数
print(array.size)   # 6
# 获得矩阵维度
print(array.ndim)   # 默认行向量，一行为一个维度
