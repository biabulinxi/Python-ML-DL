# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/25 16:11
# @File_name:demo06_LabelEncode.py
# @IDE:PyCharm

"""
标签编码
"""

import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    'audi', 'ford', 'audi', 'toyota',
    'ford', 'bmw', 'toyota', 'byd',
    'audi'])

# 创建标签编码器
lbe = sp.LabelEncoder()
# 执行标签编码
result = lbe.fit_transform(raw_samples)
print(result)

# 逆向回推原始数据
r_samples = lbe.inverse_transform(result)
print(r_samples)
