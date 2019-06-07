# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/18 11:06
# @File_name:demo03_max.py
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
dates, opening_prices, highest_prices, lowest_prices,closing_prices = np.loadtxt('../da_data/aapl.csv', delimiter=',', usecols=(1, 3, 4, 5, 6), unpack=True, dtype='M8[D], f8, f8, f8, f8',converters={1: dmy2ymd})

############################################
# 评估AAPL股票每天最高价、最低价的波动性，
max_price = np.max(highest_prices)
min_price = np.min(lowest_prices)
print(max_price, min_price)

# 查看最高价与最低价到底是那一天
max_i = np.argmax(highest_prices)
min_i = np.argmin(lowest_prices)
print(max_i, min_i)

##############################################
# 同维数组比较
a = np.arange(1,10)
b = a[::-1]
a = a.reshape(3, 3)
b = b.reshape(3, 3)
# 将两个同维数组中对应位置的元素进行比较，把最大的保留。返回新数组
print(np.maximum(a, b))
# 将两个同维数组中对应位置的元素进行比较，把最小的保留。返回新数组
print(np.minimum(a, b))

