# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/28 9:54
# @File_name:01_sk_data.py
# @IDE:PyCharm

"""
sklearn datasets
"""

from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
from sklearn.model_selection import train_test_split

#######################################################
# 获取小的数据集 load_*()
# li = load_iris()

# print('获取特征值')
# print(li.data)
# print('获取目标值')
# print(li.target)
# print(li.DESCR)  # 数据描述
# print(li.feature_names)  # 特征名称
# print(li.target_names)  # 目标名称

# 划分测试样本 返回测试集 test x_test y_test 训练集 train x_tarain y_train
# :一般划分比例 3:1
# 默认乱序
# x_train, x_test, y_train, y_test = train_test_split(li.data, li.target, test_size=0.25)
#
# print('训练集特征值和目标值：',x_train, y_train)
# print('测试集特征值和目标值：',x_test, y_test)

#################################################
# 获取大的数据集
# news = fetch_20newsgroups(subset='all')
# print(news.data)
# print(news.target)

#######################################
# 获取回归数据集
lb = load_boston()
print('获取特征值')
print(lb.data)
print('获取目标值')
print(lb.target)
print(lb.DESCR)  # 数据描述

