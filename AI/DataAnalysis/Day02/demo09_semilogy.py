# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/14 16:12
# @File_name:demo09_semilogy.py
# @IDE:PyCharm

"""
刻度网格线
"""

import matplotlib.pyplot as plt

plt.figure('Grid Line', facecolor='lightgray')

# 绘制子图
plt.subplot(121)
plt.title('Grid Line', fontsize=16)
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.tick_params(labelsize=10)

# 获取坐标轴
ax = plt.gca()
# 设置刻度定位器
ax.xaxis.set_major_locator(plt.MultipleLocator())
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(250))
ax.yaxis.set_minor_locator(plt.MultipleLocator(50))
# 绘制刻度网格线
ax.grid(which='both', axis='both',linewidth=0.75, linestyle='-', color='orange')
ax.grid(which='both', axis='both',linewidth=0.25, linestyle='-', color='orange')

y = [1,10,100,1000,100,10,1]
plt.plot(y, color='dodgerblue')

# 绘制半对数图
plt.subplot(122)
plt.title('semilogy', fontsize=16)
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.tick_params(labelsize=10)
# 获取坐标轴
ax = plt.gca()
# 设置刻度定位器
ax.xaxis.set_major_locator(plt.MultipleLocator())
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(250))
ax.yaxis.set_minor_locator(plt.MultipleLocator(50))
# 绘制刻度网格线
ax.grid(which='both', axis='both',linewidth=0.75, linestyle='-', color='orange')
ax.grid(which='both', axis='both',linewidth=0.25, linestyle='-', color='orange')

y = [1,10,100,1000,100,10,1]
plt.semilogy(y, color='dodgerblue')

plt.show()
