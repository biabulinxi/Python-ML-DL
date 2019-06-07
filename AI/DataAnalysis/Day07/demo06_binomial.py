# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/21 15:36
# @File_name:demo06_binomial.py
# @IDE:PyCharm

"""
案例： 某人投篮命中率为0.5， 投10次进5个球的概率。
"""

import numpy as np

# np.random.binomial(一个事件尝试多少次, 成功的概率, 多少个事件)
r = np.random.binomial(10,0.5,10000)
p = (r == 5).sum() / r.size
print(p)
