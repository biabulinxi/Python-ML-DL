# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/28 16:16
# @File_name:01_decision.py
# @IDE:PyCharm

"""
决策树对泰坦尼克号进行生死预测
"""

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier


def decision():
    """
    决策树对泰坦尼克号进行生死预测
    :return: None
    """
    # 获取数据
    titan = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')

    # 处理数据，找出特征值和目标值
    x = titan[['pclass', 'age', 'sex']]
    y = titan[['survived']]

    # 缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True)

    # 分割数据
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    # print(x_train)

    # 进行处理(特征工程) 特征 -> 类别 -> one_hot编码
    dic = DictVectorizer(sparse=False)
    # # todict(orient='records') 把每一行转换为字典
    x_train = dic.fit_transform(x_train.to_dict(orient='records'))
    x_test = dic.transform(x_test.to_dict(orient='records'))
    print(dic.get_feature_names())
    # print(x_train)

    # 决策树进行预测
    dec = DecisionTreeClassifier()
    dec.fit(x_train, y_train)

    # 预测准确率
    print('预测准确率', dec.score(x_test, y_test))

    # 导出决策树的结构
    export_graphviz(dec, out_file='./tree.dot', feature_names=dic.get_feature_names())

    return None


def randomforest():
    """
    随机森林对泰坦尼克号进行生死预测
    :return: None
    """
    # 获取数据
    titan = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')

    # 处理数据，找出特征值和目标值
    x = titan[['pclass', 'age', 'sex']]
    y = titan[['survived']]

    # 缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True)

    # 分割数据
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    # print(x_train)

    # 进行处理(特征工程) 特征 -> 类别 -> one_hot编码
    dic = DictVectorizer(sparse=False)
    # # todict(orient='records') 把每一行转换为字典
    x_train = dic.fit_transform(x_train.to_dict(orient='records'))
    x_test = dic.transform(x_test.to_dict(orient='records'))
    print(dic.get_feature_names())
    # print(x_train)

    # 随机森林进行预测，超参数调优
    rf = RandomForestClassifier()

    param = {'n_estimators': [120, 200, 300, 500, 800, 1200], 'max_depth': [5, 8, 15, 25, 30]}

    # 网格搜索和交叉验证
    gc = GridSearchCV(rf, param_grid=param, cv=2)

    gc.fit(x_train, y_train)

    # 预测准确率
    print('预测准确率', gc.score(x_test, y_test))
    print('查看选择的参数模型：', gc.best_params_)
    print('查看最好的得分：', gc.best_score_)

    return None


if __name__ == '__main__':
    # decision()
    randomforest()
