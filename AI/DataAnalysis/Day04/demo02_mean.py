# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/18 10:30
# @File_name:demo02_mean.py
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

plt.plot(dates, closing_prices, color='b', linewidth=3, linestyle='--', label='closing_prices', alpha=0.5)

###############################################
# 绘制均值线
mean = np.mean(closing_prices)
plt.hlines(mean, dates[0], dates[-1],color='orangered',label='Mean(ClosingP)')

###############################################
# VWAP - 成交量加权平均价格
vwap = np.average(closing_prices, weights=volumns)
plt.hlines(vwap, dates[0], dates[-1], color='g',label='VMAP')

################################################
# TWAP-时间加权平均价格
times = np.arange(1,closing_prices.size+1)
twap = np.average(closing_prices, weights=times)
plt.hlines(twap, dates[0], dates[-1], color='b',label='TMAP')

plt.legend()
# 自动格式化x轴的日期输出
plt.gcf().autofmt_xdate()
plt.show()





