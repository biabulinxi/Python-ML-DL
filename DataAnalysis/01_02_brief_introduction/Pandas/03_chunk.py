# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/19 16:32
# @File_name:03_chunk.py
# @IDE:PyCharm

import pandas as pd
import csv

file_name = 'iris.csv'

# iris_chunks = pd.read_csv(file_name, header=None, names=['C1','C2','C3','C4', 'C5'], chunksize=10)
#
###############################################
# # 将大量数据划分为区块chunk，chunksize 表示区块行数，含有chunksize，则 read_csv返回的是一个迭代器
# for chunk in iris_chunks:
#     print(chunk.shape)
#     print(chunk)


########################################
# # 定义一个迭代器来处理大量数据
# iris_chunks = pd.read_csv(file_name, header=None, names=['C1','C2','C3','C4', 'C5'], iterator=True)
#
# print(iris_chunks.get_chunk(10).shape)
# print(iris_chunks.get_chunk(20).shape)
# print(iris_chunks.get_chunk(2))

#########################################
# 

