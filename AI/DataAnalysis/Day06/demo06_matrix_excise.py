# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/20 14:39
# @File_name:demo06_matrix_excise.py
# @IDE:PyCharm

"""
案例：假设一帮人去旅游， 去程做的是大巴，小孩票价3元，大人3.2元。共花了118.4； 回来时坐火车，小孩票价3.5元，大人3.6元。共花了135.2. 求大人和小孩的人数。
"""

import numpy as np

prices = np.mat('3 3.2;3.5 3.6')
totals = np.mat('118.4;135.2')
# 最小二乘法求解线性方程
X = np.linalg.lstsq(prices, totals)[0]
print('最小二乘法求解线性方程:\n',X)
# 矩阵求解
X = prices.I * totals
print('矩阵求解:\n',X)
