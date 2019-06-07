# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/11 19:30
# @File_name:data_extraction.py
# @IDE:PyCharm

"""
完成对原始大量数据的抽取，探索分析。
"""

import pandas as pd
from sqlalchemy import create_engine


class DataProcess(object):
    def __init__(self):
        # 连接数据库
        self.engine = create_engine('mysql://root:123456@176.234.100.101:3306/e_commerce?charset=utf8')
        # 按照10000条数据进行分块，返回生成器对象sql
        self.sql = pd.read_sql('all_gzdata', self.engine, chunksize=10000)

    # 网页类型分析
    def urlIdAnalysis(self):
        """
        网址类型统计分析，分析哪类型的信息，用户访问量最多
        :return:
        """
        # 逐块统计不同网址类型的数目
        urlType_counts = [i['fullURLId'].value_counts() for i in self.sql]
        # 合并统计结果，合并相同的统计项（即按index分组求和）, 转成series
        counts = pd.concat(urlType_counts).groupby(level=0).sum()
        # 重新设置index，将原来的index用做counts的第二列，转dataframe
        counts = counts.reset_index()
        # 重新设置列名，主要是第二列，默认0
        counts.columns = ['index', 'num']
        # 利用正则表达式，提取前三个数字作为类别ID
        counts['type'] = counts['index'].str.extract('(\d{3})',expand=True)
        # 获取百分比
        counts['percent'] = counts['num']/counts('num').sum()
        # 按类别合并
        counts_ = counts[['type', 'num', 'percent']].groupby('type').sum()
        counts_['percent'] = counts_['percent'].apply(lambda x: format(x, '.4%'))
        counts_ = counts_.sort_values(by='num', ascending=False)  # 降序排列
        counts_ = counts_.reset_index()
        print(counts_)

    # 统计101类别的情况
    def count101(self, data):
        data101 = data[['fullURLId']][data['fullURLId'].str.contains('101')].copy()
        return data101['fullURLId'].value_counts()

    def workOn101(self):
        """
        其中浏览咨询内容页记录（101003）最多，其次是咨询列表页（101002）和资源首页（101001）
        :return:
        """
        # 逐块统计
        counts101 = [self.count101(i) for i in self.sql]
        # 合并统计结果
        counts101 = pd.concat(counts101).groupby(level=0).sum()
        counts101 = pd.DataFrame(counts101)
        counts101.columns = ['num']
        counts101['percent'] = counts101['num']/counts101['num'].sum()
        counts101['percent'] = counts101['percent'].apply(lambda x: format(x, ".4%"))
        # 降序排列输出
        print(counts101.sort_values('num',ascending=False))

    # 统计107类型网页内部的情况
    def ID107_count(self, data):
        url107 = data[['fullURL']][data['fullURLId'].str.contains('107')].copy()  # 找出类别包含107的网址
        url107['type'] = None  # 添加空列
        url107['type'][url107['fullURL'].str.contains('info/.+?/')] = '知识首页'
        url107['type'][url107['fullURL'].str.contains('info/.+?/.+?')] = '知识列表页'
        url107['type'][url107['fullURL'].str.contains('/\d+?_*\d+?\.html')] = '知识内容页'
        return url107['type'].value_counts()

    def workOn107(self):
        id107_counts = [self.ID107_count(i) for i in self.sql]
        id107_counts = pd.concat(id107_counts).groupby(level=0).sum()
        id107_counts = id107_counts.reset_index()
        id107_counts.columns = ['type', 'num']
        id107_counts['percent'] = id107_counts['num']/id107_counts['num'].sum()
        id107_counts['percent'] = id107_counts['percent'].apply(lambda x: format(x, '.4%'))
        print(id107_counts.sort_values('num',ascending=False))

    # 统计1999001类别的情况
    def count199(self,data):  # 自定义统计函数
        counts199 = data[['pageTitle']][data['fullURLId'].str.contains('1999001')].copy()  # 找出类别包含101的网址
        counts199['type'] = u'其他'
        counts199['type'][(counts199['pageTitle'] != '') & (counts199['pageTitle'].str.contains(u'快车-律师助手'))] = '快车-律师助手'
        counts199['type'][(counts199['pageTitle'] != '') & (counts199['pageTitle'].str.contains(u'免费发布法律咨询'))] = '免费发布咨询'
        counts199['type'][(counts199['pageTitle'] != '') & (counts199['pageTitle'].str.contains(u'咨询发布成功'))] = '咨询发布成功'
        counts199['type'][(counts199['pageTitle'] != '') & (counts199['pageTitle'].str.contains(u'快搜'))] = '快搜'
        return counts199['type'].value_counts()

    def workOn199(self):
        counts199 = [self.count199(i) for i in self.sql]  # 逐块统计
        counts199 = pd.concat(counts199).groupby(level=0).sum()  # 合并统计结果
        counts199 = pd.DataFrame(counts199)
        counts199.columns = ['num']
        counts199['percent'] = counts199['num'] / counts199['num'].sum()
        counts199['percent'] = counts199['percent'].apply(lambda x: format(x,'.4%'))
        print(counts199.sort_values('num', ascending=False))  # 降序排列

    # 网页点击次数分析
    def clickCount(self):
        # 统计真是IP出现的次数
        counts = [i['realIP'].value_counts() for i in self.sql]
        # 按index分组，合并统计结果，转成series
        realIPCounts = pd.concat(counts).groupby(level=0).sum()
        # 转成dataframe
        realIPCounts = pd.DataFrame(realIPCounts)
        realIPCounts[1] = 1  # 添加一列，全为1
        click_Counts = realIPCounts.groupby('realIP').sum()  # 统计各个‘不同的点击次数’分别出现的次数
        clickCounts = click_Counts.iloc[:7,:].append(click_Counts.iloc[7:,:].sum(),ignore_index=True)
        clickCounts.index = list(range(1,8))+['7次以上']
        print(clickCounts)
        self.countsgreater8(click_Counts)

    # 分析点击8次以上的数据
    def countsgreater8(self,data):
        countsgreater8 = pd.concat([data.iloc[7:100, :].sum(), data.iloc[100:300, :].sum(), data.iloc[300:, :].sum()])
        countsgreater8.index = ['8-100', '101-300', '301以上']
        countsgreater8 = pd.DataFrame(countsgreater8)
        countsgreater8.index.name = '点击次数'
        countsgreater8.columns = ['用户数']
        print(countsgreater8)

    # 网页排名
    def url_sort(self):
        counts4 = [i[['realIP', 'fullURL', 'fullURLId']] for i in self.sql]
        counts4_ = pd.concat(counts4)
        htmlurl = counts4_[counts4_['fullURL'].str.contains('\.html')]
        urlid = pd.DataFrame(counts4_[-counts4_['realIP'].isin(htmlurl['realIP'])].drop_duplicates('fullURL').groupby('fullURLId').size()).sort_values(by=0, ascending=False)
        print(urlid)


if __name__ == '__main__':
    dataProcess = DataProcess()
    # dataProcess.urlIdAnalysis()
    # dataProcess.workOn101()
    # dataProcess.workOn107()
    # dataProcess.workOn199()
    # dataProcess.clickCount()
    dataProcess.url_sort()
