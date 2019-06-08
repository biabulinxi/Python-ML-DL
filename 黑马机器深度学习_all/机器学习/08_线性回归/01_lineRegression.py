# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/29 9:55
# @File_name:01_lineRegression.py
# @IDE:PyCharm

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib

def mylinear():
    """
    线性回归直接预测房子价格
    :return: None
    """
    # 获取数据
    lb = load_boston()

    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target,test_size=0.25)

    # 标准化处理(目标值也需要)
    std_x = StandardScaler()
    std_y = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)
    y_train = std_y.fit_transform(y_train.reshape(-1,1))
    y_test = std_y.transform(y_test.reshape(-1,1))

    ############################################
    # estimator预测

    ##############
    # 正规方程求解方式预测结果

    # 创建并训练模型
    # lr = LinearRegression()
    # lr.fit(x_train, y_train)

    # # 模型保存
    # joblib.dump(lr,'./tmp/lr.pkl')

    # 模型加载
    lr = joblib.load('./tmp/lr.pkl')

    # 系数矩阵
    print('系数矩阵',lr.coef_)

    # 预测测试集的房子价格
    y_lr_predict = std_y.inverse_transform(lr.predict(x_test))
    print('正规方程求解方式预测测试集的房子价格:',y_lr_predict)

    ###############
    # 梯度下降房价预测
    sgd = SGDRegressor()

    sgd.fit(x_train, y_train)
    # 系数矩阵
    print('系数矩阵', sgd.coef_)

    # 预测测试集的房子价格
    y_sgd_predict = std_y.inverse_transform(sgd.predict(x_test))
    print('梯度下降预测测试集的房子价格:', y_sgd_predict)

    ###############
    # 岭回归房价预测
    rd = Ridge(alpha=10)

    rd.fit(x_train, y_train)
    # 系数矩阵
    print('系数矩阵', rd.coef_)

    # 预测测试集的房子价格
    y_rd_predict = std_y.inverse_transform(rd.predict(x_test))
    print('岭回归预测测试集的房子价格:', y_rd_predict)

    ######################################
    # 模型评估
    print('正规方程求解的均方误差：',mean_squared_error(std_y.inverse_transform(y_test),y_lr_predict))
    print('梯度下降求解的均方误差：',mean_squared_error(std_y.inverse_transform(y_test),y_sgd_predict))
    print('岭回归求解的均方误差：',mean_squared_error(std_y.inverse_transform(y_test),y_rd_predict))

if __name__ == '__main__':
    mylinear()