# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/30 11:13
# @File_name:pricipal_component_analyze.py
# @IDE:PyCharm

"""
利用主成分分析进行属性规约，对数据进行降维
"""

import pandas as pd
from sklearn.decomposition import PCA

inputfile = '../data/principal_component.xls'
outputfile = '../tmp/dimention_reduced.xls'

data = pd.read_excel(inputfile, header=None)  # 读取原始数据

pca = PCA()  # 导入PCA算法模型
pca.fit(data)  # 训练模型
feature_vectors = pca.components_  # 返回模型的各个特征向量
variance_ratios = pca.explained_variance_ratio_  # 返回各个成分的方差百分比(贡献率)

print('##############模型的各个特征向量################')
print(feature_vectors)
print('##############各个成分的方差百分比(贡献率)################')
print(variance_ratios)

variance_cumratios = []  # 累计百分率
threshold = 0.97  # 设置阈值为97%
count = 0  # 用来记录主要成分的个数
for i in variance_ratios:
    variance_cumratios.append(i)
    count += 1
    if sum(variance_cumratios) > 0.97 :
        break
print('主成分个数为count=',count)

# 利用求得的主要成分个数，重新建立PCA模型，进行属性降维
pca = PCA(count, copy=True)  # 保留的主成分个数为3，复制原数据进行建模降维
pca.fit(data)
low_d = pca.transform(data)   # 进行降维
pd.DataFrame(low_d).to_excel(outputfile)  # 保存数据
pca.inverse_transform(low_d)  # 避免源数据也降维，可用inverse_transform来复原数据
print(low_d)


