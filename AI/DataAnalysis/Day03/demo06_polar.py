# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 11:55
# @File_name:demo06_polar.py
# @IDE:PyCharm

"""
极坐标系
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 8*np.pi, 1000)
y = 0.6*x

plt.figure('Polar', facecolor='lightgray')
plt.title('Polar', fontsize=16)
plt.grid(linestyle=':')

# 极坐标下绘制
plt.gca(projection='polar')
plt.plot(x, y, color='b')
plt.show()
