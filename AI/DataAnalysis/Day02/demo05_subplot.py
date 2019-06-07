# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/14 14:52
# @File_name:demo05_subplot.py
# @IDE:PyCharm

"""
网格式布局
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as mg

plt.figure('Grid Layout', facecolor='lightgray')
gs = mg.GridSpec(3, 3)
# 第一幅： gs[行号,列号]
plt.subplot(gs[0,:2])
plt.text(0.5,0.5,'1',ha='center', va='center',size=36)
# 不显示刻度
plt.xticks([])
plt.yticks([])

# 第二幅
plt.subplot(gs[:2,2])
plt.text(0.5,0.5,'2',ha='center', va='center',size=36)
plt.xticks([])
plt.yticks([])

# 第三幅
plt.subplot(gs[1,1])
plt.text(0.5,0.5,'3',ha='center', va='center',size=36)
plt.xticks([])
plt.yticks([])

# 第四幅
plt.subplot(gs[1:,0])
plt.text(0.5,0.5,'4',ha='center', va='center',size=36)
plt.xticks([])
plt.yticks([])

# 第五幅
plt.subplot(gs[2,1:])
plt.text(0.5,0.5,'5',ha='center', va='center',size=36)
plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()
