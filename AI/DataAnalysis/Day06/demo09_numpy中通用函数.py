# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/20 15:38
# @File_name:demo09_numpy中通用函数.py
# @IDE:PyCharm

"""
numpy中通用函数
"""

import numpy as np

a = np.arange(1,10)
# #############################################
# ####数组的裁剪和压缩
# # 数组裁剪，小于最小值的修正为最小值
# print(a.clip(min=3, max=6))
# # 数组压缩, 根据条件筛选数组
# print(a.compress(a>=6))
#
# ############################################
# # 加法通用函数
# a = a.reshape(3,3)
# print('a\n', a)
# b = a[::-1]
# print(np.add(a, b))  # 求两数组之和
# print(np.add.reduce(a,axis=1))  # 求数组元素的列和axis=0或行和axis=1
# print(np.add.accumulate(a))  # 求数组元素的列和axis=0或行和axis=1 的过程数组
# print(np.add.outer([10, 20, 30],a))  # 求列表与数组的外和：把a分别加到列表的每一个元素

# ##############################################
# # 乘法通用函数
# a = a.reshape(3,3)
# b = a[::-1]
# print(a.prod())
# print(np.prod(a))  # 返回a数组中所有元素累乘的结果
# print(a.cumprod())  # 返回a数组中所有元素累乘的过程数组
# print(np.cumprod(a))  # 返回a数组中所有元素累乘的过程数组
# print(np.outer([10, 20, 30],a))  # 外积：把a分别乘到列表的每一个元素

# ##############################################
# # 除法通用函数
# a = a.reshape(3,3)
# b = a[::-1]
# print(a/b)
# print(np.divide(a, b))  # a / b
# print(np.floor_divide(a, b))  # 地板除
# print(np.ceil(a/b))  # 天花板除
# print(np.round(a/b))  # 四舍五入取整
# print(np.trunc(a/b))  # 截断除，去掉小数位

################################################
# 位运算
a = a.reshape(3,3)
b = a[::-1]

# # 位异或
# print(a^b < 0)  # 判断对应元素是否异号
# print(np.bitwise_xor(a,b) < 0)  # 判断对应元素是否异号
# 位与
print(a&(a-1) == 0)
print(a&b == 0)
print(np.bitwise_and(a, b))
# 位与求2的n次幂
print('-' * 45)
for i in range(1, 201):
    if i & (i - 1) == 0:
        print(i, end=' ')

