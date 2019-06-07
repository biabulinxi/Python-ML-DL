# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/12 15:55
# @File_name:data_preparation.py
# @IDE:PyCharm

import pandas as pd
from sqlalchemy import create_engine

"""
在原始数据探索分析的基础上，发现与分析目标无关或模型需要处理的数据，针对此类数据进行处理。其中涉及的数据处理方式有：数据清洗、数据集成、数据变换和属性规约。
"""


class DataProcess(object):
    def __init__(self):
        # 连接数据库
        self.engine = create_engine('mysql://root:123456@176.234.100.101:3306/e_commerce?charset=utf8')
        # 按照10000条数据进行分块，返回生成器对象sql
        self.sql = pd.read_sql('all_gzdata', self.engine, chunksize=10000)

    # 数据清洗
    def data_clean_save(self):
        for data in self.sql:
            # 获取网址列
            urlData = data[['realIP','fullURL']]
            # 删选出以.html结尾的详情网页地址
            urlData = urlData[urlData['fullURL'].str.contains('\.html')].copy()
            # 保存数据到cleaned_gzdata表中，若不存在，自动创建
            # urlData.to_sql('cleaned_gzdata', self.engine, index=False, if_exists='append')
            self.data_change(urlData)
        print('数据清洗完成')

    # 数据变换
    def data_change(self,data):
        # 逐块变换去重
        # 将下划线后面的网址部分去掉，规范为标准网址
        data['fullURL'] = data['fullURL'].str.replace('_\d{0,2}.html', '.html')
        # 删除重复记录
        data = data.drop_duplicates()
        # 保存数据库
        # data.to_sql('changed_gzdata', self.engine, index=False, if_exists='append')
        print('数据变换完成！')
        self.data_split(data)

    # 网址分类
    def data_split(self, data):
        data['type'] = data['fullURL']
        data['type_1'] = None
        data['type_2'] = None
        data['type'][data['fullURL'].str.contains('(ask)|(askzt)')] = '咨询'
        data['type'][data['fullURL'].str.contains('(info)|(zhishiku)')] = '知识'
        data['type'][data['fullURL'].str.contains('(faguizt)|(lifadongtai)')] = '机构'
        data['type'][data['fullURL'].str.contains('(fayuan)|(gongan)|(jianyu)|(gongzhengchu)')] = '公司'
        data['type'][data['fullURL'].str.contains('(interview)')] = '访谈'
        data['type'][data['fullURL'].str.contains('d\d+(_\d)?(_p\d+)?\.html')] = '政策'
        data['type'][data['fullURL'].str.contains('(baike)')] = '百科'
        data['type'][data['type'].str.len() > 15] = 'etc'
        data[['type_1', 'type_2']] = data['fullURL'].str.extract(
            'http://www.lawtime.cn/(info|zhishiku)/(?P<type_l_1>[A-Za-z]+)/(?P<type_l_2>[A-Za-z]+)/\d+\.html',
            expand=False).iloc[:, 1:]
        # 保存数据库
        data.to_sql('splited_gzdata', self.engine, index=False, if_exists='append')
        # print(data)
        print("网页分类完成，成功存入数据库")




if __name__ == '__main__':
    dataprocess = DataProcess()
    dataprocess.data_clean_save()