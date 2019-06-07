# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/28 17:10
# @File_name:plot_func.py
# @IDE:PyCharm

"""
数据探索中常用的做图函数
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 用来在图表中正常显示中文标签
plt.rcParams["axes.unicode_minus"] = False  # 用来在图标中正常显示负号
plt.figure(figsize=(7, 5))  # 创建图像区域，指定比例


############################################
# plot()作图函数
"""
x = np.linspace(0, 2 * np.pi, 50)  # x 坐标输入, x=(0,2pi), 设置50个点
y = np.sin(x)  # 计算对应的 x 的正弦值
plt.plot(x, y, "bp--")  # 控制图形格式为蓝色带星虚线，显示正弦曲线
plt.show()
"""


############################################
# pie() 饼形图
"""
The slices will be ordered and plotted counter-clockwise.
这些切片将被排序并逆时针绘制。
        x       :(每一块)的比例，如果sum(x) > 1会使用sum(x)归一化；
        labels  :(每一块)饼图外侧显示的说明文字；
        explode :(每一块)离开中心距离；
        startangle :起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起；
        shadow  :在饼图下面画一个阴影。默认值：False，即不画阴影；
        labeldistance :label标记的绘制位置,相对于半径的比例，默认值为1.1, 如<1则绘制在饼图内侧；
        autopct :控制饼图内百分比设置,可以使用format字符串或者format function
                '%1.1f'指小数点前后位数(没有用空格补齐)；
        pctdistance :类似于labeldistance,指定autopct的位置刻度,默认值为0.6；
        radius  :控制饼图半径，默认值为1；
        counterclock ：指定指针方向；布尔值，可选参数，默认为：True，即逆时针。将值改为False即可改为顺时针。
        wedgeprops ：字典类型，可选参数，默认值：None。参数字典传递给wedge对象用来画一个饼图。例如：wedgeprops={'linewidth':3}设置wedge线宽为3。
        textprops ：设置标签（labels）和比例文字的格式；字典类型，可选参数，默认值为：None。传递给text对象的字典参数。
        center ：浮点类型的列表，可选参数，默认值：(0,0)。图标中心位置。
        frame ：布尔类型，可选参数，默认值：False。如果是true，绘制带有表的轴框架。
        rotatelabels ：布尔类型，可选参数，默认为：False。如果为True，旋转每个label到指定的角度。
"""
"""
sizes = [15, 30, 45, 10]  # 设置每一部分所占的比例
explode = (0, 0.1, 0, 0)  # 设置突出，默认0不突出
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'  # 定义标签
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']  # 设置每一块的显示颜色

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%2.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
plt.show()
"""

############################################
# hist() 二维条形直方图
"""
x = np.random.randn(1000)  # 1000个服从正态分布的随机数
plt.hist(x, 10)  # 分成十组进行绘制直方图
plt.show()
"""

############################################
# boxplot()  样本数据箱型图
"""
x = np.random.randn(1000)  # 1000个服从正态分布的随机数
D = pd.DataFrame([x, x+1]).T  # 构造两列的DataFrame
D.plot(kind="box")   # 调用Series内置的作图方法进行画图，kind 参数指定箱型图
plt.show()
"""

############################################
# plot(logx=True/logy=True)对数图形, 默认以10为底
"""
x = pd.Series(np.exp(np.arange(20)))  # 随机生成一组10的n次方的随机数
x.plot(label="原始数据图", legend=True)
plt.show()

x.plot(logy=True, label="对数数据图", legend=True)
plt.show()
"""

############################################
# plot(yerr=error/xerr=error)  绘制误差条形图
error = np.random.randn(10)  # 定义正太分布的误差列
y = pd.Series(np.sin(np.arange(10)))  # 均值正弦数据列
y.plot(yerr=error)  # 绘制误差图
plt.show()
