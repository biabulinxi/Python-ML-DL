# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/25 15:59
# @File_name:demo05_OneHotEncode.py
# @IDE:PyCharm

"""
独热编码
"""

import numpy as np
import sklearn.preprocessing as sp

samples = np.array([
    [17, 100, 4000],
    [20, 80, 5000],
    [23, 70, 5500],
])

# 构建独热编码器
# 方法1,
# sparse=False，直接返回编码后的数组，Ture则返回编码数组的索引坐标的值，dtype 数据类型
ohe = sp.OneHotEncoder(sparse=False)
r = ohe.fit_transform(samples)
print(r)

# 方法二
# 获取ohe的编码字典
ohe_dic = ohe.fit(samples)
r = ohe_dic.transform(samples)
print(r)

