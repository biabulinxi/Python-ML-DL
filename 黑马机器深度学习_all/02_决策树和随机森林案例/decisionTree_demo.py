# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/10 16:34
# @File_name:decisionTree_demo.py
# @IDE:PyCharm

"""
决策树和随机森林案例
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets.california_housing import fetch_california_housing
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor


def data_process():
    """
    获取加利福尼亚房价数据，进行数据预处理
    :return: x_train, y_train, x_test, y_test
    """

    # 获取数据
    housing = fetch_california_housing()
    # print(housing.DESCR)  # 查看数据集描述

    # 获取特征值和目标值
    x = pd.DataFrame(housing.data,
                     columns=housing.feature_names)
    y = pd.DataFrame(housing.target, columns=['average value'])
    # print(x.head())
    # print(y.head())

    # 分割数据
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 特征工程，数据标准化, 返回数组
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.fit_transform(x_test)
    y_train = std.fit_transform(y_train).ravel()
    y_test = std.fit_transform(y_test).ravel()
    # print(x_train)
    # print(y_train)

    return x_train, x_test, y_train, y_test


def decision(x_train, x_test, y_train, y_test):
    """
    决策树，分析加利福尼亚房价预测
    :return: None
    """

    # 模型建立
    dtr = DecisionTreeRegressor()

    # 网格搜索和交叉验证调参, 预剪枝操作
    tree_params = {'max_depth': [10, 12, 15], 'max_leaf_nodes': [100, 120, 140, 160, 180, 200]}
    grid = GridSearchCV(dtr, param_grid=tree_params, cv=5)
    grid.fit(x_train, y_train)

    print('决策树预测准确率', grid.score(x_test, y_test))
    print('决策树查看选择的参数模型：', grid.best_params_)
    print('决策树查看最好的得分：', grid.best_score_)


def randomforest(x_train, x_test, y_train, y_test):
    """
    随机森林：分析加利福尼亚房价预测
    """

    # 模型建立
    rfr = RandomForestRegressor()

    # 网格搜索和交叉验证调参, 预剪枝操作 进行5折交叉验证
    tree_params = {'n_estimators': [10,50,100], 'min_samples_split': [3,6,9]}
    grid = GridSearchCV(rfr, param_grid=tree_params, cv=2)
    grid.fit(x_train, y_train)

    print('随机森林预测准确率', grid.score(x_test, y_test))
    print('随机森林查看选择的参数模型：', grid.best_params_)
    print('随机森林查看最好的得分：', grid.best_score_)


if __name__ == '__main__':
    x_train, x_test, y_train, y_test = data_process()
    decision(x_train, x_test, y_train, y_test)
    randomforest(x_train, x_test, y_train, y_test)
