# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/20 11:10
# @File_name:demo04_profit.py
# @IDE:PyCharm

"""
案例： 定义一种买进卖出策略， 通过历史数据判断这种策略是否可以实施。
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


# 加载文件
dates, opening_prices, highest_prices, lowest_prices,closing_prices = np.loadtxt('../da_data/aapl.csv', delimiter=',', usecols=(1, 3, 4, 5, 6), unpack=True, dtype='M8[D], f8, f8, f8, f8',converters={1: dmy2ymd})


# 定义一种投资策略
def profit(opening_price, highest_price, lowest_price, closing_price):
    buying_price = opening_price * 0.99
    if lowest_price <= buying_price <= highest_price:
        # 返回收率的百分比
        return (closing_price-buying_price)*100 / buying_price
    return np.nan  # 返回无效值


# 调用函数，求得收益率
profits = np.vectorize(profit)(opening_prices, highest_prices, lowest_prices, closing_prices)
print(profits)

# 判断profits中哪个数据为nan
nan = np.isnan(profits)
# dates[~nan] 按位求烦
dates, profits = dates[~nan], profits[~nan]

# 绘制收盘价
plt.figure('Profits', facecolor='lightgray')
plt.title('Profits', fontsize=18)
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

plt.plot(dates, profits, color='b', linewidth=3, label='Profits', alpha=0.5)

plt.hlines(profits.mean(), dates[0], dates[-1], color='r',linewidth=2)

plt.legend()
# 自动格式化x轴的日期输出
plt.gcf().autofmt_xdate()
plt.show()

