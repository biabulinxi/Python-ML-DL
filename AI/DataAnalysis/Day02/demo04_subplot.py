# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/14 14:39
# @File_name:demo04_subplot.py
# @IDE:PyCharm

"""
绘制子图
"""

import matplotlib.pyplot as plt

plt.figure('Subplot A', facecolor='lightgray')

for i in range(9):
    plt.subplot(3,3,i+1)
    plt.text(0.5, 0.5, i+1, ha='center', va='center', size=36, alpha=0.5)
    plt.tight_layout()
plt.show()

