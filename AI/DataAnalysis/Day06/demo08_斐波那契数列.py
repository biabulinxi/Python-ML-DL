# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/20 14:59
# @File_name:demo08_斐波那契数列.py
# @IDE:PyCharm

"""
求解菲波那切数列
"""

import numpy as np

A = np.mat('1 1;1 0')
# 矩阵A的n次方的右上角元素为菲波那切数列

for i in range(1, 30):
    print((A**i)[0,1], end=',')
