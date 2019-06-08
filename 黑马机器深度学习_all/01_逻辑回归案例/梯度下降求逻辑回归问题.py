# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/19 19:29
# @File_name:梯度下降求逻辑回归问题.py
# @IDE:PyCharm

"""
构建一个梯度下降法求解逻辑回归问题的算法
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time


class LogiReg(object):
    """
    目标：建立分类器（求解出三个参数 theta0, theta1, theta2 ）
    设定阈值，根据阈值判断录取结果。

    要完成的模块
    sigmoid : 映射到概率的函数
    model : 返回预测结果值
    cost : 根据参数计算损失
    gradient : 计算每个参数的梯度方向
    descent : 进行参数更新
    accuracy: 计算精度
    """

    def __init__(self, data):
        self.data = data
        self.STOP_ITER = 0
        self.STOP_COST = 1
        self.STOP_GRAD = 2

    def _sctter(self):
        """
        :return: 测试数据，绘制散点图
        """
        positive = self.data[self.data[
                                 'Admitted'] == 1]  # returns the subset of rows such Admitted = 1, i.e. the set of *positive* examples
        negative = self.data[self.data[
                                 'Admitted'] == 0]  # returns the subset of rows such Admitted = 0, i.e. the set of *negative* examples

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.scatter(positive['Exam1'], positive['Exam2'], s=30, c='b', marker='o', label='Admitted')
        ax.scatter(negative['Exam1'], negative['Exam2'], s=30, c='b', marker='o', label='Not Admitted')
        ax.legend()
        ax.set_xlabel('Exam1 Score')
        ax.set_ylabel('Exam2 Score')

    def sigmoid(self, z):
        """
        Sigmoid
        g:ℝ→[0,1]
        g(0)=0.5
        g(−∞)=0
        g(+∞)=1
        :param z: 自编量
        :return: sigmoid 值
        """
        return 1 / (1 + np.exp(-z))

    def model(self, X, theta):
        """
        :param X: 自变量数据矩阵
        :param theta: 待求的系数矩阵
        :return: 返回预测结果值
        """
        return self.sigmoid(np.dot(X, theta.T))

    def cost(self, X, y, theta):
        """
        将对数似然函数去负号
        D(ℎ(𝑥),𝑦)=−𝑦log(ℎ(𝑥))−(1−𝑦)log(1−ℎ(𝑥))
        求平均损失
        J(theta)=∑D(ℎ(𝑥),𝑦)
        :param X: 自变量矩阵
        :param y: 因变量矩阵
        :param theta:  待求的参数矩阵
        :return: 对数似然的平均损失
        """
        left = np.multiply(-y, np.log(self.model(X, theta)))  # 表示减号左边的式子
        right = np.multiply(1 - y, np.log(1 - self.model(X, theta)))
        return np.sum(left - right) / len(X)

    def gradient(self, X, y, theta):
        """
        公式:
        ∂J/∂theta_j=−1/m * ∑i=1_n(𝑦_i−ℎ_theta(𝑥_i))𝑥_i_j
        :param X: 自变量矩阵
        :param y: 因变量矩阵
        :param theta:  待求的参数矩阵
        :return: 计算损失函数的梯度值
        """
        grad = np.zeros(theta.shape)
        error = (self.model(X, theta) - y).ravel()
        for j in range(len(theta.ravel())):  # 遍历每一个系数参数
            term = np.multiply(error, X[:, j])
            grad[0, j] = np.sum(term) / len(X)
        return grad

    def descent(self, data, theta, batchSize, stopType, thresh, alpha):
        """
        梯度下降的求解，进行参数的更新
        :param data: 数据
        :param batchSize:  批处理大小
        :param stopType:  停止迭代的类型
        :param thresh:  停止迭代的阈值
        :param alpha:  梯度下降的步长大小
        :return:
        """

        def stopCriterion(type, value, threshold):
            """
            设置三种不同的停止迭代的策略
            :param type: 停止迭代的类型
            :param value:  迭代值
            :param threshold:  阈值
            :return:
            """
            if type == self.STOP_ITER:
                return value > threshold
            elif type == self.STOP_COST:
                return abs(value[-1] - value[-2]) < threshold
            elif type == self.STOP_GRAD:
                return np.linalg.norm(value) < threshold

        def shuffleData(data):
            """
            将数据打乱，进行洗牌
            :param data:
            :return:
            """
            np.random.shuffle(data)
            cols = data.shape[1]
            X = data[:, 0:cols - 1]
            y = data[:, cols - 1:]
            return X, y

        init_time = time.time()
        i = 0  # 迭代次数
        k = 0  # batch
        X, y = shuffleData(data)
        grad = np.zeros(theta.shape)  # 初始化梯度矩阵
        costs = [self.cost(X, y, theta)]  # 损失值

        # 进行迭代
        while True:
            grad = self.gradient(X[k:k + batchSize], y[k:k + batchSize], theta)
            k += batchSize  # 取batch数量个数据
            if k >= batchSize:
                k = 0
                X, y = shuffleData(data)  # 重新洗牌
            theta = theta - alpha * grad  # 参数更新
            costs.append(self.cost(X, y, theta))  # 计算新的损失
            i += 1

            if stopType == self.STOP_ITER:
                value = i
            elif stopType == self.STOP_COST:
                value = costs
            elif stopType == self.STOP_GRAD:
                value = grad

            if stopCriterion(stopType, value, thresh):
                break
        return theta, i - 1, costs, grad, time.time() - init_time

    def runExpe(self, data, theta, batchSize, stopType, thresh, alpha):
        """
        调用迭代函数，并进行绘图
        :param data:
        :param theta:
        :param batchSize:
        :param stopType:
        :param thresh:
        :param alpha:
        :return:
        """
        theta, iter, costs, grad, dur = self.descent(data, theta, batchSize, stopType, thresh, alpha)
        name = 'Original' if (data[:, 1] > 2).sum() > 1 else 'Scaled'
        name += 'data - learning rate: {} -'.format(alpha)
        if batchSize == batchSize:
            strDescType = 'Gradient'
        elif batchSize == 1:
            strDescType = 'Stochatic'
        else:
            strDescType = 'Mini-bath({})'.format(batchSize)
        name += strDescType + ' descent - Stop:'
        if stopType == self.STOP_ITER:
            strStop = "{} iterations".format(thresh)
        elif stopType == self.STOP_COST:
            strStop = "costs change < {}".format(thresh)
        else:
            strStop = "gradient norm < {}".format(thresh)
        name += strStop
        print("***{}\nTheta: {} - Iter: {} - Last cost: {:03.2f} - Duration: {:03.2f}s".format(name, theta, iter,
                                                                                               costs[-1], dur))
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.plot(np.arange(len(costs)), costs, 'r')
        ax.set_xlabel('Iterations')
        ax.set_ylabel('Cost')
        ax.set_title(name.upper() + ' - Error vs. Iteration')
        plt.show()
        return theta

    def predict(self, X, theta):
        """
        计算模型的精度
        """
        return [1 if x >= 0.5 else 0 for x in self.model(X, theta)]


if __name__ == '__main__':
    path = 'data' + os.sep + 'LogiReg_data.txt'
    data = pd.read_csv(path, header=None, names=['Exam1', 'Exam2', 'Admitted'])
    data.head()
    data.insert(0, 'Ones', 1)
    orig_data = data.as_matrix()
    theta = np.zeros([1, 3])

    # 数据标准化
    from sklearn import preprocessing as pp

    scaled_data = orig_data.copy()
    scaled_data[:, 1:3] = pp.scale(orig_data[:, 1:3])

    # 创建对象，进行计算
    logireg = LogiReg(data)
    logireg.runExpe(orig_data, theta, batchSize=100, stopType=0, thresh=5000, alpha=0.000001)

    # 求解模型精度
    scaled_X = scaled_data[:, :3]
    y = scaled_data[:, 3]
    predictions = logireg.predict(scaled_X, theta)
    correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predictions, y)]
    accuracy = (sum(map(int, correct)) % len(correct))
    print('accuracy = {0}%'.format(accuracy))
