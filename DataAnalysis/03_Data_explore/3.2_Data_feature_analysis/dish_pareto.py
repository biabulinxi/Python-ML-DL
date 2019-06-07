# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/28 10:52
# @File_name:dish_pareto.py
# @IDE:PyCharm

"""餐厅菜品盈利数据累计分析，帕累托图"""

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams["axes.unicode_minus"] = False    # 用来正常显示负号

# 初始化参数
dish_profit = "../data/catering_dish_profit.xls"
data = pd.read_excel(dish_profit, index_col="菜品名")
data = data["盈利"].copy()         # 提取数据中的盈利数据，略去菜品 ID
data.sort_index(ascending=False)  # 按照索引列：菜品名，进行排序

# 导入图像库
plt.figure()
data.plot(kind="bar")  # 导入第一 y 坐标盈利数据，用柱状图显示
plt.ylabel("盈利(元)")  # 设置左边 Y 坐标和标签
# 累积和/总和 = 比例，用来表示第二 y 坐标的盈利累计比例曲线
p = data.cumsum() / data.sum()
# 设置第二 y 坐标的盈利累计比例曲线的颜色，样式和线宽
p.plot(color='r', secondary_y = True, style = '-o', linewidth = 2)
# 在第二 y 坐标的盈利累计比例曲线的 85% 处添加注释，包括箭头形状
# format(p[5],".4%")，p[6]代表注释的值为累计频率点的值，从零开始索引；".4%" 表示显示的数据为百分值，保留4位小数点
# xy = (5, p[5])  # 表示添加注释的位置
# xytext = (6*0.9,p[5]*0.9)
# arrowprops = dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
# 表示注释用箭头标注,arrowstyle 表示箭头形状，connectionstyle表示箭头线的连接风格，默认直线，设置为弧度，半径为0.2
plt.annotate(format(p[5],".4%"),xy = (5, p[5]), xytext = (6*0.9,p[5]*0.9),
             arrowprops = dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.ylabel("盈利(比例)") # 设置右边 Y 坐标和标签
plt.show()
