# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/18 15:30
# @File_name:demo08_sma.py
# @IDE:PyCharm

"""
移动平均线
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

plt.plot(dates, closing_prices, color='b', linewidth=3, linestyle='--', label='closing_prices', alpha=0.3)


########################################################
# 计算5日均线
sma5 = np.zeros(closing_prices.size - 4)
for i in range(sma5.size):
    sma5[i] = closing_prices[i:i+5].mean()

# 绘制均线图
plt.plot(dates[4:],sma5, color='orangered', label='SMA-5', linewidth=2)

########################################################
# 基于卷积元算的5日均线
# 卷积核数组
core = np.ones(5) / 5
# 有效卷积运算
sma52 = np.convolve(closing_prices, core, 'valid')
plt.plot(dates[4:],sma52, color='g', label='SMA-52', linewidth=7, alpha=0.3)

# 基于卷积元算的10日均线
# 卷积核数组
core = np.ones(10) / 10
# 有效卷积运算
sma53 = np.convolve(closing_prices, core, 'valid')
plt.plot(dates[9:],sma53, color='b', label='SMA-53', linewidth=7, alpha=0.3)

###################################################
# 加权卷积5日均线
# 从 y = e^x, 取5个值作为卷积核
weights = np.exp(np.linspace(-1, 0, 5))
weights = weights[::-1]
# 权重归一化
weights /= weights.sum()
ema5 = np.convolve(closing_prices, weights, 'valid')
plt.plot(dates[4:],ema5, color='yellow', label='SMA-5wt', linewidth=2)


plt.legend()
# 自动格式化x轴的日期输出
plt.gcf().autofmt_xdate()
plt.show()


