# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/27 14:48
# @File_name:01data_preprocess.py
# @IDE:PyCharm

"""
数据进行预处理
"""

from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer
import numpy as np

def mm():
    """
    归一化处理
    :return:
    """
    mm = MinMaxScaler(feature_range=(2,3))
    data = mm.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])
    print(data)


def standard():
    """
    标准化处理
    :return:
    """
    std = StandardScaler()
    data = std.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])
    print(data)

    return None


def im():
    """
    缺失值处理
    :return:
    """
    # 按列进行平均值缺失值填补
    im = Imputer(missing_values='NaN',strategy='mean',axis=0)
    data = im.fit_transform([[1, 2], [np.nan, 3], [7, 6]])
    print(data)


if __name__ == '__main__':
    # mm()
    # standard()
    im()