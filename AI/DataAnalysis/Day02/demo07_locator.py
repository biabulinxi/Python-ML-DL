# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/14 15:47
# @File_name:demo07_locator.py
# @IDE:PyCharm

"""
刻度定位器
"""

import matplotlib.pyplot as plt

localtors = ['plt.NullLocator()','plt.MultipleLocator(1)','plt.MaxNLocator(nbins=4)']

plt.figure('Locator', facecolor='lightgray')

for i, locator in enumerate(localtors):
    plt.subplot(len(localtors), 1, i+1)
    ax = plt.gca()
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.ylim(-1,1)
    plt.xlim(-5,5)

    plt.yticks([])
    ax.spines['bottom'].set_position(('data',0))
    # 设置水平轴的主刻度定位器，隔 1
    ax.xaxis.set_major_locator(eval(locator))
    # 设置水平轴的主刻度定位器，隔 0.1
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))

plt.tight_layout()
plt.show()

