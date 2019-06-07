# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/14 14:16
# @File_name:demo03_figure.py
# @IDE:PyCharm

"""
窗口的创建
"""

import matplotlib.pyplot as plt

# title：窗口的标题
# figsize： 窗口比例
# dpi：像素大小
# facecolor：图表的背景色
plt.figure('Figure A', figsize=(4,3), dpi=60,facecolor='skyblue')
plt.figure('Figure B', facecolor='red')

# 设置窗口参数
plt.figure('Figure A')
plt.title('Figure A', fontsize=18)
plt.xlabel('X', fontsize =14)
plt.ylabel('Y', fontsize =14)
plt.tick_params(labelsize=12)
plt.grid(linestyle=':')
plt.tight_layout()

plt.show()
