# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/25 14:39
# @File_name:demo02_scaler.py
# @IDE:PyCharm

"""
范围缩放
"""

import numpy as np
import sklearn.preprocessing as sp

samples = np.array([
    [17, 100, 4000],
    [20, 80, 5000],
    [23, 70, 5500],
])

# 范围缩放器
mms = sp.MinMaxScaler(feature_range=(0, 1))
r_samples = mms.fit_transform(samples)
print(r_samples)

# 基于线性关系，实现范围缩放
linear_samples = samples.copy()
for col in linear_samples.T:
    # 一个col为原始数据的一列
    col_min = col.min()
    col_max = col.max()
    A = np.array([
        [col_min, 1],
        [col_max, 1]
    ])
    B = np.array([0, 1])
    # x = [k, b]
    x = np.linalg.lstsq(A, B)[0]
    col *= x[0]
    col += x[1]
print(linear_samples)
