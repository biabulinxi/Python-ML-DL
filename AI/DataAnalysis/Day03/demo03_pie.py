# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 10:16
# @File_name:demo03_pie.py
# @IDE:PyCharm

"""
饼状图
"""

import matplotlib.pyplot as plt

plt.figure('Languages', facecolor='lightgray')
plt.title('Languages', fontsize=16)

# 设置饼形图属性
labels = ['Python','Javascript', 'C++','Java','PHP']
spaces = [0.05,0.01,0.01,0.01,0.01]
values = [26,17,21,25,5]
colors = ['dodgerblue','orangered','limegreen','violet','gold']

# 设置等轴拉伸
plt.axis('equal')
plt.pie(
    values,        # 值列表
    spaces,        # 扇形之间的间距列表
    labels,         # 标签列表
    colors,         # 颜色列表
    '%.2f%%',      # 标签所占比例的格式化字符串
    shadow=True,    # 是否添加阴影
    startangle=90,   # 起始角度
    radius=1         # 大饼半径
)
plt.show()
