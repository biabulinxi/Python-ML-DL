# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 16:41
# @File_name:demo12_gen.py
# @IDE:PyCharm

"""
模拟心电图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ma

# 初始化图形
plt.figure('Signal', facecolor='lightgray')
plt.title('Signal', fontsize=16)
plt.xlim(0, 10)
plt.ylim(-3, 3)
plt.grid(linestyle=':')
# plot 返回元组
pl = plt.plot([], [], color='dodgerblue', label='Signal')[0]


# 启动动画
def update(data):
    t, v = data
    x, y = pl.get_data()       # x, y 为数组
    x = np.append(x, t)
    y = np.append(y, v)
    # 重新绘制图形
    pl.set_data(x, y)
    # 移动坐标轴
    if x[-1] > 10:
        plt.xlim(x[-1]-10, x[-1])


x = 0
def generator():
    global x
    y = np.sin(2*np.pi*x) * np.exp(np.sin(0.2 * np.pi * x))
    yield (x, y)
    x += 0.05


anim = ma.FuncAnimation(plt.gcf(), update, generator, interval=30)
plt.legend()
plt.show()
