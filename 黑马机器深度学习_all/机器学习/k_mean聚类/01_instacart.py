# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/28 8:47
# @File_name:01_instacart.py
# @IDE:PyCharm

"""
探究：用户对物品类别的喜好细分降维
tip: 数据庞大，计算时间过长，计算机配置不高的建议，04_分布式计算
"""

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# 读取四张表的数据
prior = pd.read_csv('./data/order_products__prior.csv')
products = pd.read_csv('./data/products.csv')
orders = pd.read_csv('./data/orders.csv')
aisles = pd.read_csv('./data/aisles.csv')


# 合并四张表到一张表
_mg = pd.merge(prior,products,on=['product_id','product_id'])
_mg = pd.merge(_mg,orders, on=['order_id','order_id'])
mt = pd.merge(_mg, aisles, on=['aisle_id','aisle_id'])

mt.head()

# 交叉表(特殊的分组形式)  crosstab(行，列)
pd.crosstab(mt['user_id'],mt['aisle'])

# 进主成分分析
pca = PCA(n_components=0.9)
data = pca.fit_transform(cross)
# print(data)

# 把样本数据减少
x = data[:50]

# kMeans聚类
km = KMeans(n_clusters=4)
km.fit(x)
predict = km.predict(x)

# 显示聚类的结果
plt.figure(figsize=(10,10))

# 建立四个颜色列表
colors = ['y','g','b','r']
color = [colors[i] for i in predict]

plt.scatter(x[:,1],x[:,20],color=color)
plt.xlabel('1')
plt.xlabel('20')
plt.show()


# 评判聚类效果，轮廓系数

print(silhouette_score(x,predict))
