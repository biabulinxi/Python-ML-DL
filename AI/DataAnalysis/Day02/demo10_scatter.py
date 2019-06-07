# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/14 17:23
# @File_name:demo10_scatter.py
# @IDE:PyCharm

"""
散点图
"""

import matplotlib.pyplot as plt
import numpy as np

n = 500
# 随机生成500个样本身高, np.random.normal(期望, 标准差, 个数)
x = np.random.normal(172, 20, n)
# 随机生成500个样本体重
y = np.random.normal(65, 10, n)

plt.figure('Persons', facecolor='lightgray')
plt.title('Person points', fontsize=16)
plt.xlabel('Height',fontsize=12)
plt.ylabel('Weight',fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')

# cmap='jet' 颜色映射方式
d = (x-172)**2 + (y-65)**2
plt.scatter(x, y, c=d, cmap='jet', color='dodgerblue', alpha=0.5, label='Person')
plt.legend()
plt.show()
