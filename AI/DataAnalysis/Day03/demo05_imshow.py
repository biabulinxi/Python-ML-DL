# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 11:07
# @File_name:demo05_imshow.py
# @IDE:PyCharm

"""
热成像图
"""

import numpy as np
import matplotlib.pyplot as plt

# 生成网格点坐标矩阵
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))

# 根据x,y计算当前坐标下的z的高度值
z = (1-x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

# 设置图形属性
plt.figure('Contour', facecolor='lightgray')
plt.title('Contour', fontsize=18)
plt.xlabel('X', fontsize=14)
plt.ylabel('Y', fontsize=14)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')

# 绘制热成像图
plt.imshow(z,cmap='jet',origin='lower')
plt.show()
