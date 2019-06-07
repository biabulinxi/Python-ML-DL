# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/18 14:09
# @File_name:demo05_std.py
# @IDE:PyCharm

"""
绘制均值线
"""

import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as md


# 处理日期格式
def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    # 转换格式
    d = dt.datetime.strptime(dmy, '%d-%m-%Y')
    t = d.date()
    s = t.strftime('%Y-%m-%d')
    return s


# usecols = (列索引,)
dates, closing_prices, volumns= np.loadtxt('../da_data/aapl.csv', delimiter=',', usecols=(1, 6, 7), unpack=True, dtype='M8[D], f8, f8,',converters={1: dmy2ymd})

# 获取收盘价的标准差
print(np.std(closing_prices))   # 总体标准差
print(np.std(closing_prices, ddof=1))   # 样本标准差，自由度减少1

# 自己算总体标准差
mean = np.mean(closing_prices)
std = np.sqrt(np.mean((closing_prices - mean) ** 2))
print(std)
