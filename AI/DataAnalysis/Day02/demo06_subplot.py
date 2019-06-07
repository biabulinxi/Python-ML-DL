# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/14 15:31
# @File_name:demo06_subplot.py
# @IDE:PyCharm

"""
自有布局的子图
"""

import matplotlib.pyplot as plt

plt.figure('Flow Layout', facecolor='lightgray')

# 设置图表的位置，需要给出左下角点坐标与宽、高即可
plt.axes([0.1,0.1,0.5,0.3])
plt.text(0.5,0.5,'1',ha='center',va='center',size=36)

plt.axes([0.1,0.5,0.5,0.3])
plt.text(0.5,0.5,'2',ha='center',va='center',size=36)

plt.show()