# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/18 8:45
# @File_name:01_data_loading.py
# @IDE:PyCharm

import pandas as pd
from urllib import request

# 从 url 网上获取文件
# url = "http://aima.cs.berkeley.edu/data/iris.csv"
# iris_file = request.urlopen(url)

# 从文件读取
iris_file = 'iris.csv'

iris = pd.read_csv(iris_file, sep=',', decimal='.', header=None,
                         names=['sepal_length', 'sepal_width',
                                'petal_lenght', 'petal_width', 'target'])
# # 获取前五行数据
# print(iris.head())
# # 获取前两行数据
# print(iris.head(2))
# # 获取数据框的所有字段标题
# print(iris.columns)

# 获取一列数据
Y = iris['target']
# print(Y)
print(Y.shape)
# 获取多列数据
X = iris[['sepal_length', 'sepal_width']]
# print(X)
print(X.shape)