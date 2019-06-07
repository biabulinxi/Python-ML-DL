# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/2/25 16:56
# @File_name:discrete_point_test.py
# @IDE:PyCharm

"""
使用 k-Means 算法聚类消费行为特征数据
"""

import pandas as pd
import numpy as np

# 参数初始化
inputfile = '../data/consumption_data.xls'
k = 3  # 聚类类别
threshold = 2  # 离群点阈值
iteration = 500  # 聚类最大循环次数
data = pd.read_excel(inputfile,index_col='Id')  # 读取数据
data_zs = 1.0 * (data - data.mean())/data.std()  # 数据标准化

from sklearn.cluster import KMeans
model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)  # 建立模型
model.fit(data_zs)  # 训练模型

# 标准化数据及其类别
r = pd.concat([data_zs, pd.Series(model.labels_,index=data.index)],axis=1)  # 每个样本对应的类别
r.columns = list(data.columns) + ["聚类类别"]

norm = []
for i in range(k):
    norm_tmp = r[['R','F','M']][r['聚类类别'] == i] - model.cluster_centers_[i]
    norm_tmp = norm_tmp.apply(np.linalg.norm,axis=1)  # 求绝对距离
    norm.append(norm_tmp/norm_tmp.median())  # 求相对距离并添加

norm = pd.concat(norm)  # 合并

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

norm[norm <= threshold].plot(style='go')  # 正常点
discrete_points = norm[norm > threshold]
discrete_points.plot(style='ro')  # 离群点

# 对离群点进行标记
for i in range(len(discrete_points)):
    id = discrete_points.index[i]
    n = discrete_points.iloc[i]
    plt.annotate('(%s,%.2f)'%(id,n), xy = (id,n), xytext = (id,n))

plt.xlabel('编号')
plt.ylabel('相对距离')
plt.show()



