# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 11:07
# @File_name:demo04_contour.py
# @IDE:PyCharm

"""
等高线
"""

import numpy as np
import matplotlib.pyplot as plt

# 生成网格点坐标矩阵
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))

# 根据x,y计算当前坐标下的z的高度值
z = (1-x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

# 绘制等高线
plt.figure('Contour', facecolor='lightgray')
plt.title('Contour', fontsize=18)
plt.xlabel('X', fontsize=14)
plt.ylabel('Y', fontsize=14)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')

cntr = plt.contour(x, y, z, colors='black', linewidths=0.5)
# cntr 返回等高线对象绘制标注
plt.clabel(cntr, inline_spacing=1, fmt='%.2f', fontsize=10)
# 为登高线填充颜色
plt.contourf(x, y, z, 10, cmap='jet')

plt.show()
