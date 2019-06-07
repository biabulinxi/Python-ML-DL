# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/19 14:27
# @File_name:demo03_cnv.py
# @IDE:PyCharm

"""
协方差
"""

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

# 收盘线
plt.plot(dates, vale_closing_prices, color='b', linewidth=1, linestyle='--', label='vale_prices',alpha=0.5)
plt.plot(dates, bhp_closing_prices, color='r', linewidth=1, linestyle='--', label='bhp_prices',alpha=0.5)

##################################################
# 计算两组数据的协方差
vale_mean = np.mean(vale_closing_prices)
bhp_mean = np.mean(bhp_closing_prices)
dev_vale = vale_closing_prices - vale_mean
dev_bhp = bhp_closing_prices - bhp_mean
vale_bhp_cov = np.mean(dev_vale * dev_bhp)
bhp_vale_cov = np.mean(dev_bhp * dev_vale )
print('vale_bhp协方差为：',vale_bhp_cov)
print('bhp_vale协方差为：',bhp_vale_cov)

#####################################################
# 计算两只股票的相关性系数
k = vale_bhp_cov / (np.std(vale_closing_prices) * np.std(bhp_closing_prices))
print('相关性系数为:',k)

########################################################
# 求解两组数据的相关性系数矩阵
coef_matrix = np.corrcoef(vale_closing_prices, bhp_closing_prices)
print('相关系数矩阵：\n',coef_matrix)

########################################################
# 求解两组数据的协方差,返回的协方差矩阵即是相关系数矩阵的分子矩阵
cov_matrix = np.cov(vale_closing_prices, bhp_closing_prices)
print('协方差矩阵：\n',cov_matrix)
# 样本均值的分母不同，相差1，所以数据有所偏差

plt.legend()
# 自动格式化x轴的日期输出
plt.gcf().autofmt_xdate()
plt.show()
