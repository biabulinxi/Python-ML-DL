# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/18 17:30
# @File_name:demo09_bld.py
# @IDE:PyCharm



"""
绘制布林带
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


###################################################
# 加权卷积5日均线
# 从 y = e^x, 取5个值作为卷积核
weights = np.exp(np.linspace(-1, 0, 5))
weights = weights[::-1]
# 权重归一化
weights /= weights.sum()
ema5 = np.convolve(closing_prices, weights, 'valid')
plt.plot(dates[4:],ema5, color='b', label='SMA-5wt', linewidth=2, alpha=0.8)

######################################################
# 绘制布林带
# 获取标准差矩阵
stds = np.zeros(ema5.size)
for i in range(stds.size):
    stds[i] = closing_prices[i:i+5].std()

# 计算上下轨,并绘制
uppers = ema5 + 2 * stds
lowers = ema5 - 2 * stds
plt.plot(dates[4:],uppers, color='r', label='uppers', linewidth=2)
plt.plot(dates[4:],lowers, color='r', label='lowers', linewidth=2)

# 填充布林带
plt.fill_between(dates[4:], uppers, lowers, uppers > lowers, color='b', alpha=0.3, label='bld')


plt.legend()
# 自动格式化x轴的日期输出
plt.gcf().autofmt_xdate()
plt.show()


