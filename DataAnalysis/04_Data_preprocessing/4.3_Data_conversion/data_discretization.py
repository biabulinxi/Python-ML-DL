# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/29 14:41
# @File_name:data_discretization.py
# @IDE:PyCharm

"""
数据离散化：对连续的数据进行离散分类
分别用等宽法、等频法、一维聚类对数据进行离散化，将数据分为4类，然后将每一类记为
同一个标记，如分别记为A1、A2、A3、A4，在进行建模
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

datafile = "../data/discretization_data.xls"
data = pd.read_excel(datafile)  # 读取数据
data = data["肝气郁结证型系数"].copy()  # 去掉数据的表头,转换成一个一维series
k = 4  # 设置分类数为4

########################
# 等宽离散化，各个类别依次命名为0,1,2,3
d1 = pd.cut(data, k ,labels=range(k))   # 将一维数据分成4等分，labels 给每一部分面元添加标签，从0到3

########################
# 等频离散化
w = [1.0*i/k for i in range(k+1)]  # 获取频率列表[0.0, 0.25, 0.5, 0.75, 1.0]，为百分位数
w = data.describe(percentiles = w)[4:4+k+1]  # 使用describe函数返回的数据字典，从第4个数据到第8个数据，为自动计算的分位数
d2 = pd.cut(data, w, labels=range(k))  # 按照data的四分位数作为边界，进行分类

########################
# 一维聚类（cluster）离散化
# 利用 K-Means 算法
kmodel = KMeans(n_clusters=k, n_jobs=4)  # 建立模型，n_clusters为聚类(簇)数，n_jobs是并行CPU数，一般等于CPU数较好
kmodel.fit(data.reshape((len(data),1)))  # 将数据转置为行数据，训练模型
c = pd.DataFrame(kmodel.cluster_centers_).sort(0)  # 输出每个聚类的中心值，并且排序(默认无序)
n = pd.rolling_mean(c, 2).iloc[1:]  # 相邻两项求中点，作为边界点
n = [0] + list(w[0]) + [data.max()]  # 加入首末边界点
d3 = pd.cut(data, w, labels=range(k))


def cluster_plot(d, k):
    plt.rcParams["font.sans-serif"] = "SimHei"  # 用来正常显示中文标签
    plt.rcParams["axes.unicode_minus"] = False  # 打开坐标轴的负号编码，用来正常显示负号

    plt.figure(figsize=(8,3))
    for j in range(0, k):
        plt.plot(data[d==j], [j for i in d[d==j]], 'o')

    plt.ylim(-0.5, k-0.5)
    return plt


cluster_plot(d1, k).show()
cluster_plot(d2, k).show()
cluster_plot(d3, k).show()
