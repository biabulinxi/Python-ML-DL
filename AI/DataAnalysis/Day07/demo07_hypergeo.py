# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/21 15:54
# @File_name:demo07_hypergeo.py
# @IDE:PyCharm

import numpy as np


# 超几何分布
# 7个好苹果、3个坏苹果中随机抽出4个苹果,抽10次
# 抽中好苹果的数量

r = np.random.hypergeometric(7, 3, 4, 10)
p = (r==2).sum() /r.size
print(p)