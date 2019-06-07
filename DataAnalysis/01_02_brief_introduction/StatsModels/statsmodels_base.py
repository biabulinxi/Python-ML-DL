# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/24 17:00
# @File_name:statsmodels_base.py
# @IDE:PyCharm

"""利用StatsModels进行ADF平稳性检验"""

from statsmodels.tsa.stattools import adfuller as  ADF
import numpy as np

# 返回 ADF 值， P 值
print(ADF(np.random.rand(100)))