# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/25 15:40
# @File_name:demo04_binarize.py
# @IDE:PyCharm

"""
二值化
"""

import numpy as np
import sklearn.preprocessing as sp

samples = np.array([
    [17, 100, 4000],
    [20, 80, 5000],
    [23, 70, 5500],
])

# 获取二值化器，设定阈值
binarizer = sp.Binarizer(threshold=80)
r_samples = binarizer.transform(samples)
print(r_samples)
