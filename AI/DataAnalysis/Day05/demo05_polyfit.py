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
dates, bhp_closing_prices = np.loadtxt('../da_data/bhp.csv', delimiter=',', usecols=(1, 6), unpack=True, dtype='M8[D], f8,',converters={1: dmy2ymd})

# 加载vale收盘价
vale_closing_prices = np.loadtxt('../da_data/vale.csv', delimiter=',', usecols=(6), unpack=True)

# 绘制收盘价
plt.figure('COV DEMO', facecolor='lightgray')
plt.title('COV DEMO', fontsize=18)
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

# bhp与vale的离差，差价
diff = bhp_closing_prices - vale_closing_prices

# 差价曲线
plt.plot(dates, diff, color='b', linewidth=1, linestyle='--', label='diff_prices',alpha=0.5)


##################################################
# 使用四阶多项式拟合 差价diff 曲线
days = dates.astype('M8[D]').astype(int)

# 获取系数矩阵
coe = np.polyfit(days, diff, 4)
print(coe)
# 计算理论值
theory_y = np.polyval(coe, days)
# 绘制拟合曲线
plt.plot(dates, theory_y, c='orangered', linewidth=2, label='Polyfit_line')

plt.legend()
# 自动格式化x轴的日期输出
plt.gcf().autofmt_xdate()
plt.show()
