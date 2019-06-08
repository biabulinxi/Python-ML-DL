# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/28 8:47
# @File_name:02_instacart.py
# @IDE:PyCharm

"""
探究：用户对物品类别的喜好细分降维
tip: 数据庞大，计算时间过长，计算机配置不高的建议，04_分布式计算
"""

import pandas as pd
from sklearn.decomposition import PCA

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
print(data)
