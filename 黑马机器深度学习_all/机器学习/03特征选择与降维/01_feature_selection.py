# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/27 15:47
# @File_name:01_feature_selection.py
# @IDE:PyCharm

"""
对数据进行主成分分析和特征选择
"""

from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA


def var():
    """
    方差阈值选择，删除低方差特征
    :return:
    """
    var = VarianceThreshold(threshold=0.02)

    data = var.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])
    print(data)


def pca():
    """
    主成分分析进行特征降维
    :return:
    """
    # n_components降维后特征保留的百分比
    pca = PCA(n_components=0.9)
    data = pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])
    print(data)


if __name__ == '__main__':
    # var()
    pca()


