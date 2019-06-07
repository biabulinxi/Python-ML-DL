# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/14 9:38
# @File_name:demo01_plot.py
# @IDE:PyCharm

"""
基本绘图API
"""

import numpy as np
import matplotlib.pyplot as plt


xarray = np.array([2,8,5,3,9,8,2])
yarray = np.array([1,5,4,6,3,7,1])
plt.plot(xarray, yarray)

# 绘制水平垂直线
plt.vlines(3,2,8)
plt.hlines(3,2,8)

plt.show()
