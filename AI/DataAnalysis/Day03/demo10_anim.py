# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 14:59
# @File_name:demo10_anim.py
# @IDE:PyCharm

"""
简单动画
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ma


def update(number):
    print(number)

plt.figure('Animation')
# 启动动画， interval=30:每30毫秒执行一次update函数
anim = ma.FuncAnimation(plt.gcf(), update, interval=30)
plt.show()
