# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/18 14:49
# @File_name:demo07_aaa.py
# @IDE:PyCharm

# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/18 14:26
# @File_name:demo06_dp.py
# @IDE:PyCharm


"""
测试数组轴向汇总的相关API
"""

import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as md


ary = np.random.uniform(0, 10, (3, 5))
ary = ary.astype(int)
print(ary)


# 轴向汇总
def func(data):
    print('data:',data)
    return data.mean(), data.max(), data.min()

# 根据轴向的设定，把每一行（列）依次传递给func函数实现统计业务
# func： 处理函数
# axis： 轴向  0(列)  1(行)
# array： 原二维数组
r = np.apply_along_axis(func, 1, ary)
print(r)