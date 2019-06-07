# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/20 17:30
# @File_name:demo10_方波合成.py
# @IDE:PyCharm

"""
案例：合成方波：基函数:  y= 4/(2n −1)π * sin((2n−1)x)
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 1000)

y1 = 4*np.pi * np.sin(x)
y2 = 4/3*np.pi * np.sin(3*x)
y3 = 4/5*np.pi * np.sin(5*x)

# 叠加1000个波形
n = 1000
y = 0
for i in range(1, n + 1):
    y += 4 * np.pi / (2 * i - 1) * np.sin((2 * i - 1) * x)


plt.grid(linestyle=':')
plt.plot(x, y, color='r', linewidth=2)
plt.show()