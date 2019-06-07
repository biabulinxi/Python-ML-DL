# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/23 19:29
# @File_name:numpy_base_handle.py
# @IDE:PyCharm

import numpy as np

a = np.array([2, 0, 1, 5])  # 创建数组
print(a)  # 输出数组

print(a[:3])  # 输出数组的前三个元素，切片操作
print(a.min())  # 输出数组 a 的最小值
print("将数组a的元素排序，并赋值给数组a",a.sort())  # 将数组 a 的元素排序，并赋值给数组 a

b = np.array([[1, 2, 3], [4, 5, 6]])  # 创建二维数组矩阵
print("输出数组的平方阵",b*b)  # 输出数组的平方阵
