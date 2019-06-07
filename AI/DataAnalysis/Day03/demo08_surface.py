# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 14:26
# @File_name:demo08_surface.py
# @IDE:PyCharm

"""
三维曲面图
"""

# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 11:07
# @File_name:demo07_wireframe.py
# @IDE:PyCharm

"""
三维线框图
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# 生成网格点坐标矩阵
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))

# 根据x,y计算当前坐标下的z的高度值
z = (1-x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)


# 绘制3D线框图
# 设置图形属性
plt.figure('Surface', facecolor='lightgray')
ax3d = plt.gca(projection='3d')
ax3d.set_xlabel('X', fontsize=14)
ax3d.set_ylabel('Y', fontsize=14)
ax3d.set_zlabel('Z', fontsize=14)
ax3d.plot_surface(x, y, z, rstride=10, cstride=10, cmap='jet')
plt.show()

