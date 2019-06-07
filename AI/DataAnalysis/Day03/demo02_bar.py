# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 9:54
# @File_name:demo02_bar.py
# @IDE:PyCharm

"""
柱状图
"""

import numpy as np
import matplotlib.pyplot as plt

# 十二个月，苹果手机销量
x = np.arange(1,13)
apples = [42,85,18,67,41,86,54,78,35,62,93,45]
oranges = [67,38,85,18,54,89,35,98,44,16,46,52]

# 设置属性
plt.figure('Bar Chart', facecolor='lightgray')
plt.title('Bar Chart', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Num', fontsize=14)
plt.tick_params(labelsize=10)
plt.grid(linestyle=":")

# 绘图
plt.bar(x+0.2, apples, 0.4, color='limegreen', label="Apple")
plt.bar(x-0.2, oranges, 0.4, color='orange', label="Apple")

# 设置刻度
plt.xticks(x,['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

plt.legend()
plt.show()


