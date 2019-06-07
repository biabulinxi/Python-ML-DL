# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 9:34
# @File_name:demo01_fill.py
# @IDE:PyCharm

"""
图形区域填充
"""

import numpy as np
import matplotlib.pyplot as plt

n = 1000
x = np.linspace(0, 8*np.pi, n)

sin_x = np.sin(x)
cos_x = np.cos(x)

# 设置图形窗口属性
plt.figure(facecolor='lightgray')
plt.title('Fill', fontsize=16)
plt.xlabel('X',fontsize=12)
plt.ylabel('Y',fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')

# 绘图
plt.plot(x, sin_x, color='dodgerblue', label=r'$y=sin(x)$')
plt.plot(x, cos_x, color='orangered', label=r'$y=cos(x)$')

# 颜色填充
plt.fill_between(x, sin_x, cos_x, sin_x>cos_x, color='deepskyblue', alpha=0.5)
plt.fill_between(x, sin_x, cos_x, sin_x<cos_x, color='orangered', alpha=0.5)

# 显示标签，图形
plt.legend()
plt.show()
