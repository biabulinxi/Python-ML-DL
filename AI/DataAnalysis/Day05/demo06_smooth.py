# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/19 17:22
# @File_name:demo06_smooth.py
# @IDE:PyCharm

# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/19 16:16
# @File_name:demo05_polyfit.py
# @IDE:PyCharm


"""
案例：使用多项式函数拟合两只股票bhp、vale收盘价的差价函数。
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


# 加载bhp收盘价
dates, bhp_closing_prices = np.loadtxt('../da_data/bhp.csv', delimiter=',', usecols=(1, 6), unpack=True,
                                       dtype='M8[D], f8,', converters={1: dmy2ymd})

# 加载vale收盘价
vale_closing_prices = np.loadtxt('../da_data/vale.csv', delimiter=',', usecols=(6,), unpack=True)

# 绘制收盘价
plt.figure('Profit', facecolor='lightgray')
plt.title('Profit', fontsize=18)
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

##############################################
# 数据处理
# 获取收益率，np.diff()返回每两个元素的差值
bhp_returns = np.diff(bhp_closing_prices) / bhp_closing_prices[:-1]
vale_returns = np.diff(vale_closing_prices) / vale_closing_prices[:-1]
dates = dates[:-1]

# 收益率曲线
plt.plot(dates, bhp_returns, color='b', linewidth=1, label='bhp_returns', alpha=0.5)
plt.plot(dates, vale_returns, color='r', linewidth=1, label='vale_returns', alpha=0.5)

# 卷积降噪
# 汉宁窗是一个加权余弦窗函数
core = np.hanning(8)
# 归一化
core /= core.sum()
bhp_returns_convolved = np.convolve(bhp_returns, core, 'valid')
vale_returns_convolved = np.convolve(vale_returns, core, 'valid')

plt.plot(dates[7:], bhp_returns_convolved, c='b', linewidth=2, label='bhp_convolved')
plt.plot(dates[7:], vale_returns_convolved, c='r', linewidth=2, label='vale_convolved')

plt.legend()
# 自动格式化x轴的日期输出
plt.gcf().autofmt_xdate()
plt.show()
