# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/20 11:52
# @File_name:demo05_matrix.py
# @IDE:PyCharm

"""
矩阵运算
"""

import numpy as np

ary = np.arange(1, 10).reshape(3, 3)

#######################################
# 创建数组
# 方式一：np.matrix(ary) 默认复制一份数据进行运算
mat1 = np.matrix(ary)
mat1[0, 0] = 999
print(ary)
print(mat1, type(mat1))

# 方拾2：np.mat(ary)，不复制数据
mat2 = np.mat(ary)
mat2[0, 0] = 888
print(ary)
print(mat2)

# 方式3：np.mat('1 2 3; 4 5 4; 6 4 3')，分号为一行
mat3 = np.mat('1 2 3; 4 5 4; 6 4 3')
print(mat3)

##################################################
# 矩阵乘法
# 1. 矩阵 X 标量
print(mat3 * 10)
print(mat3.dot(10))
# 2. m_n矩阵乘n_s矩阵
print(mat3 * mat2)
print(mat2.dot(mat3))

################################################
# 矩阵的逆
print(mat3)
print(mat3.I)
print(np.linalg.inv(mat3))
# A * A^-1 = E
print(mat3 * mat3.I)
print(mat3 * np.linalg.inv(mat3))
# 矩阵是否可逆
mat4 = np.mat('1 2 3;2 4 6;3 6 9')
# print(mat4.I)  报错：Singular matrix，奇异矩阵
mat5 = np.mat('1 2 3;5 3 6')
print(mat5.I)  # 二维广义逆矩阵
print(np.linalg.inv(mat5))  # 默认矩阵必须为方阵才能求逆
