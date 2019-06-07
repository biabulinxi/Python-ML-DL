# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/19 16:05
# @File_name:demo04_ploy.py
# @IDE:PyCharm

"""
案例：求多项式  y = 4x^3 + 3x^2 - 1000x + 1 的驻点坐标
"""

import numpy as np
import matplotlib.pyplot as plt

# 初始化参数
x = np.linspace(-20, 20, 1000)
y = 4*x**3 + 3*x**2 - 1000*x + 1

#####################################
# 求驻点坐标
# 系数矩阵
P = np.array([4, 3, -1000, 1])
# 求导
dev = np.polyder(P)
# 驻点坐标
stag_x = np.roots(dev)
stag_y = np.polyval(P, stag_x)

plt.plot(x, y, color='b')
# 散点图 ，marker: 大小， zorder: 层级
plt.scatter(stag_x, stag_y, s=50, marker='s', c='red', zorder=3)
plt.show()