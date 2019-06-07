# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/29 9:51
# @File_name:lagrange_newton_interpolate.py
# @IDE:PyCharm

"""
拉格朗日插值对，餐厅销售额数据进行清洗
由于lagrange和newton插值在本质上是一致的，所以scipy中只提供lagrange插值函数
"""

import pandas as pd
from scipy.interpolate import lagrange  # 导入拉格朗日插值函数

inputfile = "../data/catering_sale.xls"  # 导入原始数据
outputfile = "../tmp/sales.xls"          # 输出处理完的数据

data = pd.read_excel(inputfile)  # 读取数据
# 根据之前的箱型图分析，过滤异常值，将其变为空值
data.loc[(data["销量"] < 400) | (data["销量"] > 5000),"销量"] = None


def ployinterp_column(s,n,k=5):
    """
    自定义列向量插值函数
    :param s: 字段列向量
    :param n: 被插值的位置
    :param k: 取被插值前后的5个数据，进行拉格朗日插值多项式计算
    :return: 插值并返回插值结果
    """
    y = s[list(range(n-k,n)) + list(range(n+1,n+1+k))]  # 在锁定的字段列取被插值前后的5个数据
    y = y[y.notnull()]  # 剔除空值
    return lagrange(y.index, list(y)) (n)  # 自变量取索引编号，因变量为销量，插值并返回插值结果


# # 逐个元素判断是否需要插值
# for column in data.columns:   # 遍历每一列字段值，列名
#     if column == "销量":       # 只对缺失的销量值进行插值
#         for i in range(len(data)):  # 直接遍历所有数据的位置
#             if (data[column].isnull())[i]:  # 判断销量列的每一个数据是空值则插值
#                 data.loc[i,[column]] = ployinterp_column(data[column], i)
#                 print("插入成功")


# 逐个元素判断是否需要插值
"""只对销量列的数据进行处理，减少代码冗余，节省计算机内存资源"""
for i in range(len(data["销量"])):  # 直接遍历所有数据的位置
    if (data["销量"].isnull())[i]:  # 判断销量列的每一个数据是空值则插值
        data.loc[i,["销量"]] = ployinterp_column(data["销量"], i)
        print("插入成功")

print(data)
# 输出结果，写入文件
data.to_excel(outputfile)
print("写入文件成功")
