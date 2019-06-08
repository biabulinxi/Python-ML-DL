# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/16 10:19
# @File_name:01_GMM.py
# @IDE:PyCharm

"""
基于EM算法的GMM聚类
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA

data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
# print(data.head())

# 绘制原始数据，查看基本分布
data.plot()
# 重采样数据绘制
data.resample('w').sum().plot()
data.resample('D').sum().rolling(365).sum().plot()
data.groupby(data.index.time).mean().plot()
plt.xticks(rotation=45)
plt.show()

# 数据预处理
data.columns = ['West', 'East']
data['Total'] = data['West'] + data['East']
pivoted = data.pivot_table('Total', index=data.index.time, columns=data.index.date)
pivoted.plot(legend=False, alpha =0.01);
plt.xticks(rotation=45)
plt.show()

# 数据降维
x = pivoted.fillna(0).T.values
x_2 = PCA(2).fit_transform(x)
plt.scatter(x_2[:,0], x_2[:,1])
plt.show()

# 创建GMM模型
gmm = GaussianMixture(2)
gmm.fit(x)
labels_1 = gmm.predict_proba(x)
labels_2 = gmm.predict(x)
plt.scatter(x_2[:,0],x_2[:,1], c=labels_2, cmap='rainbow')
plt.show()

# 映射回原始数据查看分类后的分布
fig, ax = plt.subplots(1, 2, figsize=(14, 6))
pivoted.T[labels_2 == 0].T.plot(legend=False, alpha=0.1, ax=ax[0])
pivoted.T[labels_2 == 1].T.plot(legend=False, alpha=0.1, ax=ax[1])
ax[0].set_title('Purple Cluster')
ax[1].set_title('Red Cluster')

plt.show()
