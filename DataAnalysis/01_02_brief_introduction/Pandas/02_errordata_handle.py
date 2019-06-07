# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/18 8:45
# @File_name:01_data_loading.py
# @IDE:PyCharm

import pandas as pd
from urllib import request


iris_file = 'iris_error.csv'

fake_dataset = pd.read_csv(iris_file, sep=',', decimal='.', parse_dates=[0])

# # pandas 会自动识别表字段，对空数据会自动填写 NaN，parse_dates=[0]可自动识别日期数据
# print(fake_dataset)
#
# # fillna() 方法可填补空数据, mean(axis=0/1)方法获取行(0)列(1)平均值，median() 获取中位值
# print("###############################################\n",fake_dataset.fillna(0))
# print("###############################################\n",fake_dataset.fillna(fake_dataset.mean(axis=0)))
# print("###############################################\n",fake_dataset.fillna(fake_dataset.mean(axis=1)))
# print("###############################################\n",fake_dataset.fillna(fake_dataset.median(axis=0)))
# print("###############################################\n",fake_dataset.fillna(fake_dataset.median(axis=1)))

# error_bab_lines 可自动去除损坏的数据行
iris_file = 'iris_error2.csv'
fake_dataset2 = pd.read_csv(iris_file, sep=',', decimal='.', parse_dates=[0], error_bad_lines=False)
print(fake_dataset2)