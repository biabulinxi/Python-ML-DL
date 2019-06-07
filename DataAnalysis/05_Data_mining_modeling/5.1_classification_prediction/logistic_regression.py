# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/30 14:51
# @File_name:logistic_regression.py
# @IDE:PyCharm

"""
对某银行在降低贷款拖欠率的数据进行逻辑回归建模
选择稳定性选择方法中的随机逻辑回归进行特征筛选，然后利用筛选后的特征建立逻辑回归模型，输出平均正确率
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR


# 参数初始化
filename = '../data/bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:, :8].as_matrix()  # 前八列数据作为自变量
y = data.iloc[:, 8].as_matrix()  # 以是否违约作为因变量，取值范围为0,1

# 建立随机逻辑回模型，筛选变量
rlr = RLR()
rlr.fit(x, y)  # 训练模型
# rlr.get_support()用来获取特征筛选结果，返回前八列数据的布尔值，筛选去掉False的数据
# 也可通过.scores_ 方法获取各个特征的分数
print("通过随机逻辑回归模型筛选特征结束")
# 筛选去掉前八列数据中随机逻辑回归为False的数据，筛选出模型特征数据
xdata = data.iloc[:, :8].columns[rlr.get_support()]
print("有效特征为：%s" % ','.join(xdata))

# 获取筛选好的特征数据，并转换为矩阵
x = data[xdata].as_matrix()

# 利用筛选好的特征，建立逻辑回归模型
lr = LR()
lr.fit(x, y)  # 用筛选后的特征数据训练模型
print("逻辑回归模型训练结束")
print("模型的平均正确率为：%s" % lr.score(x, y))  # 给出模型平均正确率
