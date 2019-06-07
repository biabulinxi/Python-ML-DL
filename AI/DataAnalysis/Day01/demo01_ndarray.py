# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/13 10:08
# @File_name:demo01_ndarray.py
# @IDE:PyCharm

"""
测试ndarray对象
"""

import numpy as np

ary = np.array([1,2,3,4,5])
print(ary)
print(type(ary))
ary = ary + 10  # 给每个元素都进行运算
print(ary)