# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/28 17:22
# @File_name:exercise.py
# @IDE:PyCharm

"""
对莺尾花数据进行分类处理
"""

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report


def iris():
    """
    对莺尾花数据进行分类处理
    :return: None
    """
    # 加载数据
    iris = load_iris()
    x = iris.data
    y = iris.target

    # print(x)
    # print(iris.DESCR)

    # 拆分数据
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    #####################################################
    def knn():
        # k-近邻模型预测分析
        knn = KNeighborsClassifier()
        param = {'n_neighbors': [1, 2, 5, 8, 10]}

        # 交叉验证和网格搜索
        gc = GridSearchCV(knn, param_grid=param, cv=10)

        # 训练模型
        gc.fit(x_train, y_train)

        # 模型准确率
        print('knn模型准确率:', gc.score(x_test, y_test))
        print('knn最优模型参数：', gc.best_estimator_)

    def naviebayes():
        # 朴素贝叶斯模型预测分析
        mlt = MultinomialNB()

        # 训练模型
        mlt.fit(x_train, y_train)
        # 模型预测
        y_predict = mlt.predict(x_test)
        # 模型准确率
        print('bayes模型准确率:', mlt.score(x_test, y_test))
        # 每个类别的精确率和召回率
        print('bayes每个类别的精确率和召回率:\n', classification_report(y_test, y_predict, target_names=iris.target_names))

    knn()
    naviebayes()

    return None


if __name__ == '__main__':
    iris()
