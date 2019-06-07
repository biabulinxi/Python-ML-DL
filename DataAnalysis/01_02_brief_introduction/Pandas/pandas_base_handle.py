# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/24 16:06
# @File_name:pandas_base_handle.py
# @IDE:PyCharm

import pandas as pd

# 创建一个序列 s
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# 创建一张表
d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
# 用已有的序列创建表格
d2 = pd.DataFrame(s)

print(s)
print(d)
print(d2)
# 预览表的前5行
print(d.head())
# 基本数据统计量
print(d.describe())


# 读取excel文件，创建DataFrame
excel_file = pd.read_excel('arima_data.xls')
print(excel_file)

# 读取 csv文本文件，需指定编码格式
csv_file = pd.read_csv('iris_error.csv', encoding='utf-8')
print(csv_file)