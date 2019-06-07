# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/13 9:43
# @File_name:model.py
# @IDE:PyCharm

"""
利用预处理的数据，进行建模。主要采用协同过滤的基于物的算法，采用杰卡德相似系数衡量其相似度，完成用户点击网页后的相关网页推荐。
"""

import pandas as pd
from sqlalchemy import create_engine
import numpy as np


class Recommender:
    sim = None

    # 定义杰卡德系数
    def jaccard(self, a, b):
        return abs(((a + b) // 2).sum()) / abs(np.ceil((a + b) / 2).sum())

    # 计算相似度矩阵
    def similarity(self, x, distance):
        y = np.ones((len(x), len(x)))
        for i in range(len(x)):
            for j in range(len(x)):
                y[i, j] = distance(x[i], x[j])
        return y

    # 训练数据
    def fit(self, x, ):
        distance = self.jaccard
        self.sim = self.similarity(x, distance)

    # 推荐系统
    def recommend(self, a):
        return np.dot(self.sim, a)


class ModelAnalysis(object):
    def __init__(self):
        # 连接数据库
        self.engine = create_engine('mysql://root:123456@176.234.100.101:3306/e_commerce?charset=utf8')
        # 按照10000条数据进行分块，返回生成器对象sql
        self.sql = pd.read_sql('splited_gzdata', self.engine, chunksize=10000)

    def sample(self):
        """
        获取婚姻相关的数据，进行协同推荐
        :return:
        """
        data = [i for i in self.sql]
        sample = pd.concat(data)
        sample = pd.DataFrame(sample)
        data = pd.crosstab(sample[sample['type_1'] == 'hunyin']['realIP'],
                           sample[sample['type_1'] == 'hunyin']['fullURL'])
        return data

    def model(self):
        r = Recommender()
        data = self.sample()
        data_ = data.values
        r.fit(data_.T)
        realid = 500271579
        uid = list(data.index).index(realid)
        sim_sort = pd.Series(r.recommend(data_[uid])).sort_values(ascending=False)
        vind = sim_sort[sim_sort >= 1].index
        ind = sim_sort[(sim_sort > 0) & (sim_sort < 1)].index
        recommenddata = pd.DataFrame(
            {'访问页面': '\n'.join(data.columns[i] for i in vind), '推荐页面': '\n'.join(data.columns[i] for i in ind[:5])},
            index=[realid], columns=['访问页面', '推荐页面'])
        recommenddata.to_excel('推荐网页.xls')


if __name__ == '__main__':
    model = ModelAnalysis()
    model.model()
