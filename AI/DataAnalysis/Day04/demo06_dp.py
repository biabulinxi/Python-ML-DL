# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/18 14:26
# @File_name:demo06_dp.py
# @IDE:PyCharm


"""
统一每个周一、周二、.. 周五的收盘价的平均值，并放入一个数组。
"""

import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as md


# 处理日期格式, 返回数字
def dmy2weekday(dmy):
    dmy = str(dmy, encoding='utf-8')
    # 转换格式
    d = dt.datetime.strptime(dmy, '%d-%m-%Y')
    t = d.date()
    wday = t.weekday()
    return wday


# usecols = (列索引,)
dates, closing_prices = np.loadtxt('../da_data/aapl.csv', delimiter=',', usecols=(1, 6,), unpack=True, dtype='f8, f8,',converters={1: dmy2weekday})


# 创建一个空数组，用来存放均价
ave_closing_prices = np.zeros(5)
# 掩码删选，进行存放
for wday in range(ave_closing_prices.size):
    ave_closing_prices[wday] = closing_prices[dates==wday].mean()

print(np.round(ave_closing_prices, 2))

