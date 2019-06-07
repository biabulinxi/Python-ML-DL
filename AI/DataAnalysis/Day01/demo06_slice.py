# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/13 15:58
# @File_name:demo06_slice.py
# @IDE:PyCharm

"""
数组切片
"""

import numpy as np
a = np.arange(1, 10)
print(a)
print(a[:3])
print(a[3:6])
print(a[6:])
print(a[::-1])
print(a[:-4:-1])
print(a[-4:-7:-1])
print(a[-7::-1])
print(a[::])
print(a[::3])
print(a[1::3])
print(a[2::3])

# ary[ : : , ：：,]
# 以逗号作为分隔符，分别对 页、行、列进行切片
a = a.reshape(3, 3)
print(a)
print(a[:2, :2])
print(a[:, 2])  # 所有行的最后一列