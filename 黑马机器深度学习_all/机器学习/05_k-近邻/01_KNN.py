# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/28 10:54
# @File_name:01_KNN.py
# @IDE:PyCharm

"""
k近邻算法， Facebook 入住位置
"""

from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler


def knncls():
    """
    K-近邻预测用户签到位置
    :return: None
    """
    # 读取数据
    data = pd.read_csv('./data/train.csv')
    # print(data.head())

    # 处理数据
    # 1.缩小数据,查询数据筛选
    data = data.query('x > 1.0 & x < 1.25 & y > 2.5 & 2.75')
    # 2.处理时间戳
    time_value = pd.to_datetime(data['time'], unit='s')
    # print(time_value)
    # 把日期格式转换为字典格式
    time_value = pd.DatetimeIndex(time_value)
    # 3.构造一些特征
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday
    # 4.把时间戳删除
    data = data.drop(['time'], axis=1)
    # 5.把签到数量小于n个目标位置进行删除
    place_count = data.groupby('place_id').count()
    tf = place_count[place_count.row_id > 3].reset_index()
    data = data[data['palce_id'].isin(tf.place_id)]

    # 6.取出数据当中的特征值和目标值, 将无关特征值row_id删除
    y = data['place_id']
    x = data.drop(['place_id','row_id'], axis=1)

    # 7.分割数据
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    #############################################################
    # 特征工程（标准化）
    std = StandardScaler()
    # 对测试集和训练集的特征值进行标准化
    x_train = std.fit_transform(x_train)
    x_test = std.fit_transform(x_test)

    #############################################################
    # # 算法流程，建立模型
    knn = KNeighborsClassifier(n_neighbors=5)
    #
    # # fit,predict, score
    # knn.fit(x_train, y_train)
    #
    # # 得出预测结果
    # y_predict = knn.predict(x_test)
    # print('预测目标签到位置为：', y_predict)
    #
    # # 评估精度得分，准确率
    # print('模型预测准确率为：', knn.score(x_test, y_test))

    # 网格测试
    # 构造一些参数的值
    param = {'n_neighbors':[1,3,5,10]}

    gc = GridSearchCV(knn,param_grid=param, cv=10)
    gc.fit(x_train,y_train)

    # 预测准确率
    print('在测试集中的准确率:',gc.score(x_test,y_test))

    print('在交叉验证当中最好的结果：',gc.best_score_)
    print('选择最好的模型是：',gc.best_estimator_)
    print('每个超参数每次交叉验证的结果：',gc.cv_results_)

    return None


if __name__ == '__main__':
    knncls()
