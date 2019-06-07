# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/20 10:38
# @File_name:demo02_piecewise.py
# @IDE:PyCharm

"""
数组处理函数
"""

import numpy as np

a = np.array([50,60,80,45,30,60,74])
# '不及格','刚及格','及格':-1, 0, 1
# ary = np.piecewise(原数组，条件序列，取值序列) ，取值序列必须为证书
b = np.piecewise(a, [a<60, a==60, a>60], [-1, 0, 1])
print(b)