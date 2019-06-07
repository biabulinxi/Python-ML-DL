# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/25 15:28
# @File_name:abnormal_check.py
# @IDE:PyCharm

"""餐饮销售额数异常检测"""

import pandas as pd
import matplotlib.pyplot as plt

# 导入餐饮数据
catering_sale = '../data/catering_sale.xls'
# 读取数据，指定“日期”列为索引
data = pd.read_excel(catering_sale, index_col=u"日期")
# 查看数据结构的基本结构
# count   200.000000     非空值的数量
# mean   2755.214700     平均值
# std     751.029772     标准差
# min      22.000000     最小值
# 25%    2451.975000     四分位数
# 50%    2655.850000
# 75%    3026.125000
# max    9106.440000     最大值
print(data.describe())

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 建立图像
plt.figure()
# 画箱线图，直接使用DataFrame的方法
p = data.boxplot(return_type='dict')
x = p['fliers'][0].get_xdata()  # 'fliers' 为异常指标签
y = p['fliers'][0].get_ydata()
y.sort()  # 从小到大排序，该方法直接改变原对象

# 用ancotate添加注释
# 其中有些相近的点，注解会出现重叠，难以看清，需要一些技巧来控制
# 一下参数是经过调试的，其他问题需要具体问题具体调试
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]),
                     xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]),
                             y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]),
                     xytext=(x[i] + 0.08, y[i]))
plt.show()  # 展示箱线图
