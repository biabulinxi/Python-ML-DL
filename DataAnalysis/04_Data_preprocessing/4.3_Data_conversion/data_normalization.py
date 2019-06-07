# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/29 14:07
# @File_name:data_normalization.py
# @IDE:PyCharm

"""
数据规范化：消除指标之间的量纲和取值范围差异的影响
对n个记录p个属性的数据集，进行规范化操作
"""

import pandas as pd
import numpy as np

datafile = "../data/normalization_data.xls"
data = pd.read_excel(datafile, header=None)  # 读取数据


# 最小-最大(离差)标准化
data = (data - data.min())/(data.max() - data.min())
print("离差标准化:\n",data)

# 零-均值(标准差)标准化
data = (data - data.mean())/data.std()
print("标准差标准化:\n",data)

# 小数定标规范化
# np.ceil(a) np.floor(a) : ceiling向上取整，floor向下取整
data = data/10**np.ceil(np.log10(data.abs().max()))
print("小数定标规范化:\n",data)


