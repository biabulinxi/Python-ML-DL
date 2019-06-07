# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/18 9:34
# @File_name:demo01_K.py
# @IDE:PyCharm


"""
加载文件，绘制股市K线图
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
# 绘制K线图
# 颜色设置,返回bool数组
rise = closing_prices >= opening_prices
# 填充色
color = np.array([('White' if x else 'limegreen') for x in rise])
# 边缘色
ecolor = np.array([('r' if x else 'g') for x in rise])

# 绘制影线
# 方法一
# plt.bar(dates, highest_prices-lowest_prices, 0.1, opening_prices, color=ecolor)

plt.vlines(dates, lowest_prices, highest_prices, color=ecolor)

# 绘制实体
# plt.bar(自变量, 高度, 宽度, 基准高度, 颜色)
plt.bar(dates, closing_prices-opening_prices, 0.8, opening_prices, edgecolor=ecolor, color=color, zorder=3)


plt.legend()
# 自动格式化x轴的日期输出
plt.gcf().autofmt_xdate()
plt.show()

