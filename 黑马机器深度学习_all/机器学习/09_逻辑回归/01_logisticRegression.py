# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/29 14:49
# @File_name:01_logisticRegression.py
# @IDE:PyCharm

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.externals import joblib


def logistic():
    """
    逻辑回归做二分类进行癌症预测（根据细胞的属性特征）
    :return: None
    """
    # 构造列标签
    column = ['示例代码编号ID编号','团块厚度','细胞大小的均匀性','细胞形状的均匀性','边际附着力','单个上皮细胞大小','裸核','布兰德染色质','正常核仁','有丝分裂','类:( 2为良性，4为恶性）']

    # 读取数据
    data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',names=column)
    # print(data)

    # 缺失值处理, 删除
    data = data.replace(to_replace='?',value=np.nan)

    data = data.dropna()

    # 进行数据的分割
    x_train, x_test, y_train, y_test = train_test_split(data[column[1:-1]],data[column[-1]],test_size=0.25)

    # 标准化处理
    std = StandardScaler()

    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 逻辑回归预测
    lg = LogisticRegression(penalty='l2',C=1.0)
    lg.fit(x_train,y_train)

    print('模型系数：',lg.coef_)
    print('准确率：',lg.score(x_test,y_test))

    print('召回率：',classification_report(y_test,lg.predict(x_test),labels=[2,4],target_names=['良性','恶性']))

    return None



if __name__ == '__main__':
    logistic()