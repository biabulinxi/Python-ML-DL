# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/13 16:07
# @File_name:demo07_mask.py
# @IDE:PyCharm

"""
nadarray 的掩码操作
"""

import numpy as np

a = np.arange(1, 10)
# 掩码操作返回布尔值，根据掩码删选元素
mask = (a % 2 == 0)
print(a)
print(mask)
print(a[mask])
# 利用掩码排序，掩码存放索引下标
mask = [8,7,0,4,1,2,3,5,6]
print(a[mask])

# 输出100以内3和7的倍数
ary1 = np.arange(1, 100)
print(ary1[(ary1 % 3 == 0) & (ary1 % 7 == 0)])
