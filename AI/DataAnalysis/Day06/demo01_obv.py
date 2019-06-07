# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 17:34
# @File_name:demo01_obv.py
# @IDE:PyCharm

"""
OBV能量潮
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
dates, closing_prices, volums= np.loadtxt('../da_data/aapl.csv', delimiter=',', usecols=(1, 6, 7), unpack=True, dtype='M8[D], f8, f8',converters={1: dmy2ymd})

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

########################################################
# 绘制OBV能量潮
diff_prices = np.diff(closing_prices)
sign_prices = np.sign(diff_prices)  # 符号化差价
# 根据符号差价设置颜色
up_obvs = volums[1:][sign_prices>=0]
up_dates = dates[1:][sign_prices>=0]
down_obvs = volums[1:][sign_prices==-1]
down_dates = dates[1:][sign_prices==-1]

plt.bar(up_dates, up_obvs, 0.8, color='r', label='OBV')
plt.bar(down_dates, down_obvs, 0.8, color='g', label='OBV')


plt.legend()
# 自动格式化x轴的日期输出
plt.gcf().autofmt_xdate()
plt.show()
