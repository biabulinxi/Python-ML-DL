# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/6 12:58
# @File_name:data_explore.py
# @IDE:PyCharm

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans  # 导入k-均值聚类算法
import matplotlib.pyplot as plt


class DataAnalysis():
    def __init__(self):
        self.datafile = '../data/air_data.csv'
        self.explorefile = '../tmp/explore.xls'
        self.cleanedfile = '../tmp/cleaned.xls'
        self.zscoredfile = '../tmp/zscored.xls'
        self.extractfile = '../tmp/extract.xls'

    def data_explore(self):
        data = pd.read_csv(self.datafile, encoding='utf-8')  # 读取原始数据
        explore = data.describe(percentiles=[], include='all').T  # 获取数据基本特征，并转置方便查阅
        explore['null'] = len(data) - explore['count']  # count 为describe函数中自动计算的非空数据个数，计算空值数
        explore = explore[['null','max','min']]  # 获取各个属性值的 空值数目，最大值，最小值
        explore.columns = ['空值数目', '最大值', '最小值']  #表头重命名
        # 导出数据探索的结果
        # explore.to_excel(self.explorefile)

    def data_cleaned(self):
        data = pd.read_csv(self.datafile, encoding='utf-8')  # 读取原始数据
        data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()]  # 剔除票价的空值

        # 只保存票价非零的数据，或者平均折扣率和总飞行公里数为0的数据
        index1 = data['SUM_YR_1'] != 0
        index2 = data['SUM_YR_2'] != 0
        index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0)
        data = data[index1 | index2 | index3]
        self.data_extract(data)
        # 写出文件
        # data.to_excel(self.cleanedfile)

    def data_extract(self,data):
        '''
        根据航空公司的LRFMC模型分析，选择保留与其相关的6个属性：FFP_DATE, LOAD_TIME，FLIGHT_COUNT，AVG_DISCOUNT，SEG_KM_SUM, LAST_TO_END，删除其他不相关属性和弱相关属性
        :return:
        '''
        # 提取LRFMC
        # 进行日期相减获取月份数
        data['L'] = (pd.to_datetime(data['LOAD_TIME']) - pd.to_datetime(data['FFP_DATE'])).dropna()
        data['L'] = data['L'].map(lambda x: x / np.timedelta64(1 * 60 * 60 * 24 * 30, 's'))
        data = data[['L','LAST_TO_END','FLIGHT_COUNT','SEG_KM_SUM','avg_discount']]
        data.columns = ['L','R','F','M','C']
        self.data_standard(data)
        # 写出文件
        # data.to_excel(self.extractfile, index=False)

    def data_standard(self,data):
        '''
        数据标准化处理
        :param data:
        :return:
        '''
        data = (data-data.mean(axis=0)) / (data.std(axis=0))
        data.columns = ['Z'+i for i in data.columns]  # 重命名表头
        # data.to_excel(self.zscoredfile, index=False)

    def workOn(self):
        self.data_explore()
        self.data_cleaned()


class Model(object):
    def __init__(self):
        self.inputFile = '../tmp/zscored.xls'
        self.classesNum = 5

    def kmodel(self):
        # 读取数据
        data = pd.read_excel(self.inputFile)
        # 调用k-means算法，进行聚类分析
        kmodel = KMeans(n_clusters=self.classesNum,n_jobs=4)
        kmodel = kmodel.fit(data) # 训练模型
        # print(kmodel.cluster_centers_)  # 查看聚类中心
        # print(kmodel.labels_)  # 查看个样本对应的类别
        return kmodel


class ClusterPlot(object):
    '''
    画出特征雷达图
    '''
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    def __init__(self,data,kmodel):

        self.labels = data.columns  # 标签
        self.k = 5  # 数据个数
        self.plot_data = kmodel.cluster_centers_
        self.color = ['b', 'g', 'r', 'c', 'y']  # 指定颜色

        self.angles = np.linspace(0, 2 * np.pi, self.k, endpoint=False)
        self.plot_data = np.concatenate((self.plot_data, self.plot_data[:, [0]]), axis=1)  # 闭合
        self.angles = np.concatenate((self.angles, [self.angles[0]]))  # 闭合

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)  # polar参数！！
        for i in range(len(self.plot_data)):
            ax.plot(self.angles, self.plot_data[i], 'o-', color=self.color[i], label=u'客户群' + str(i), linewidth=2)  # 画线
        ax.set_rgrids(np.arange(0.01, 3.5, 0.5), np.arange(-1, 2.5, 0.5), fontproperties="SimHei")
        ax.set_thetagrids(self.angles * 180 / np.pi, self.labels, fontproperties="SimHei")
        plt.legend(loc=4)
        plt.show()


if __name__ == '__main__':
    data_analysis = DataAnalysis()
    data_analysis.workOn()
    model = Model()
    kmodel = model.kmodel()
    data = pd.read_excel('../tmp/zscored.xls')
    clusterPlot = ClusterPlot(data,kmodel)
    clusterPlot.plot()



