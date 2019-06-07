# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/19 10:36
# @File_name:demo01_linalg.py
# @IDE:PyCharm


"""
线性运算，线性方程组求解
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
dates, closing_prices = np.loadtxt('../da_data/aapl.csv', delimiter=',', usecols=(1, 6), unpack=True, dtype='M8[D], f8',
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

plt.plot(dates, closing_prices, color='b', linewidth=3, linestyle='--', label='closing_prices', alpha=0.3)

#########################################################
# 基于线性模型， 实现线性预测

# 三元一次方程组
N = 3

# 定义预测数组
pred_vals = np.zeros(closing_prices.size - 2 * N + 1)
# 获取预测数组
for i in range(pred_vals.size):
    # 获取自变量矩阵 A
    A = np.zeros((N, N))
    # A[行索引，列索引]
    for j in range(N):
        A[j,] = closing_prices[j + i:i + j + N]
    # 因变量值矩阵
    B = closing_prices[i + N:i + N * 2]
    # 求解线性方程组,最小二乘法求解系数矩阵
    x = np.linalg.lstsq(A, B)[0]
    # B点乘x,矩阵乘法，预测下一个点的值
    pred = B.dot(x)
    pred_vals[i] = pred

# 绘制预测曲线图
plt.plot(dates[2*N:],pred_vals[:-1],'o-',color='red',label='Predict Prices')

plt.legend()
# 自动格式化x轴的日期输出
plt.gcf().autofmt_xdate()
plt.show()
