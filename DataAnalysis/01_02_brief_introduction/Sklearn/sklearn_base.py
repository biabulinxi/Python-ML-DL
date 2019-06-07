# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/24 17:35
# @File_name:sklearn_base.py
# @IDE:PyCharm

"""SVM 分类预测"""

from sklearn import datasets  # 导入数据集
from sklearn import svm  # 导入 SVM 模型


iris = datasets.load_iris()  # 加载数据集
print(iris)
print(iris.data.shape)  # 查看数据集

clf = svm.LinearSVC()  # 建立线性SVM分类器
model = clf.fit(iris.data, iris.target)  # 用数据训练模型

# 利用训练好的模型，用新数据进行预测
iris_predict = clf.predict([[5.0, 3.6, 1.3, 0.25]])
print(iris_predict)
# 查看训练好模型的参数
print(clf.coef_)

