# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/20 14:50
# @File_name:demo07_matrix_equation.py
# @IDE:PyCharm

"""
案例：解线性方程组
x −2y+z=0
2y −8z −8=0
−4x+5y+9z+9=0
"""

import numpy as np

cov = np.mat('1 2 1;0 2 -8;-4 5 9')
Y = np.mat('0;8;-9')

# 最小二乘法求解
X = np.linalg.lstsq(cov, Y)[0]
print(X)
X = np.linalg.solve(cov, Y)
print(X)

# 矩阵求解
X = cov.I * Y
print(X)

