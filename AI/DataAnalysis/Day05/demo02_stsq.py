# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/19 10:36
# @File_name:demo01_linalg.py
# @IDE:PyCharm


"""
 案例：利用线性拟合画出股价的趋势线。
股价的趋势线 = (最高价+最低价+收盘价) / 3
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
dates, highest_prices, lowest_price, closing_prices = np.loadtxt('../da_data/aapl.csv', delimiter=',', usecols=(1, 4, 5, 6), unpack=True, dtype='M8[D], f8, f8, f8',
                                   converters={1: dmy2ymd})

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

# 计算所有的趋势点
trend_points = (closing_prices + highest_prices + lowest_price) / 3

# 收盘线
plt.plot(dates, closing_prices, color='b', linewidth=3, linestyle='--', label='closing_prices')
# 趋势线
plt.plot(dates, trend_points, color='r', linewidth=3, linestyle='--', label='TrendPoints')

# 线性拟合
days = dates.astype('M8[D]').astype(int)
# 获得自编量矩阵
A = np.column_stack((days, np.ones(days.size)))
# 获得因变量
B = trend_points
# 计算系数矩阵，
x = np.linalg.lstsq(A, B)[0]
# 绘制线性拟合的趋势线 k=x[0], b=x[1]
trend_line = days*x[0] + x[1]
plt.plot(dates, trend_line, color='g', label='TrendLine', linewidth=2)

plt.legend()
# 自动格式化x轴的日期输出
plt.gcf().autofmt_xdate()
plt.show()
