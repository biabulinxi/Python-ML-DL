# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 14:35
# @File_name:demo09_scatter.py
# @IDE:PyCharm

"""
三维散点图
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

n = 1000
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
z = np.random.normal(0,1,n)

d = np.sqrt(x**2 + y**2 + z**2)
plt.figure('3D Scatter')
ax3d = plt.gca(projection='3d')
ax3d.set_xlabel('x', fontsize=14)
ax3d.set_ylabel('y', fontsize=14)
ax3d.set_zlabel('z', fontsize=14)
ax3d.scatter(x, y, z, s=60, alpha=0.6, c=d, cmap='jet')
plt.show()
