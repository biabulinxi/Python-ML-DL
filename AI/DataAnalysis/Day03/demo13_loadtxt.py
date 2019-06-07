# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 17:34
# @File_name:demo13_loadtxt.py
# @IDE:PyCharm

"""
加载文件
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


# usecols = (列索引, 行索引)
dates, closing_prices = np.loadtxt('../da_data/aapl.csv', delimiter=',', usecols=(1, 6), unpack=True, dtype='M8[D], f8',converters={1: dmy2ymd})

# 绘制收盘价
plt.figure('AAPL', facecolor='lightgray')
plt.title('AAPL', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')

# 设置主刻度定位器为每周一
ax = plt.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%Y/%m/%d'))

# 修改dates的数据类型 从M8[D] -> 到matplotlib可以识别的日期类型
dates = dates.astype(md.datetime.datetime)

plt.plot(dates, closing_prices, color='b', linewidth=3, linestyle='--', label='closing_prices')
plt.legend()
# 自动格式化x轴的日期输出
plt.gcf().autofmt_xdate()
plt.show()
