# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/28 14:46
# @File_name:statistic_funcs.py
# @IDE:PyCharm

"""
常用的数据特征挖掘分析函数
"""

import pandas as pd
import numpy as np

# 创建两行七列的DataFrame
data = pd.DataFrame([range(1,8),range(2,9)],columns=('a','b','c','d','e','f','g'))
print(data)
# 样本每列和
print("#############和sum()##############")
print(data.sum())
# 样本每列的平均数
print("#############平均值mean()##############")
print(data.mean())
# 样本每列的方差
print("#############方差var()##############")
print(data.var())
# 样本的每列的标准差
print("#############方差std()##############")
print(data.std())
# 相关系数
print("#############相关系数矩阵corr()##############")
print(data.corr(method="spearman"))
s1 = data["a"]
s2 = data["b"]
s1_corr_s2 = s1.corr(s2, method="pearson")
print("a与b的相关系数：",s1_corr_s2)
# 协方差
data2 = pd.DataFrame(np.random.rand(6,5))  # 生成6x5的随机矩阵
print(data2)
print("#############协方差cov()##############")
print(data2.cov())
print("第一列与第二列的协方差:",data2[0].cov(data2[1]))  # 计算第一列与第二列的协方差
# 偏度和峰度
print("#############偏度skew()##############")
print(data2.skew())   # 偏度，表示非对称数据偏离中心的程度，三阶中心距
print("#############峰度kurt()##############")
print(data2.kurt())   # 峰度，表示概率分布曲线在平均值处峰值高低的特征数，表示尖度

##############################
# 基本数据统计量
print("#############基本数据统计量##############")
print(data2.describe())

###############################
# 累计特征函数,加前缀cum，包含cumsum(),cumprod()累计积,cummax(),cummin()
data3 = pd.Series(range(20))
# 前n项的积
print("############前n项的积##############")
print(data3.cumprod())

###############################
# pandas 内建的回滚统计特征函数，加前缀rolling,如：rolling_sum()
# 依次计算相邻两项的和
print("############依次计算相邻两项的和##############")
print(pd.rolling_sum(data3,2))
