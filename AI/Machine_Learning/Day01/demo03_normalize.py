# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/25 15:09
# @File_name:demo03_normalize.py
# @IDE:PyCharm

"""
归一化
"""

import numpy as np
import sklearn.preprocessing as sp

samples = np.array([
    [17, 100, 4000],
    [20, 80, 5000],
    [23, 70, 5500],
])

r = sp.normalize(samples, norm='l1')
print(r)


