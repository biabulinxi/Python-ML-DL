# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/25 14:26
# @File_name:demo01_scale.py
# @IDE:PyCharm

"""
均值移除
"""

import numpy as np
import sklearn.preprocessing as sp

samples = np.array([
    [17,100,4000],
    [20,80,5000],
    [23,70,5500],
])

return_samples = sp.scale(samples)
print(return_samples)
print(np.mean(return_samples,axis=0))
print(np.std(return_samples,axis=0))
