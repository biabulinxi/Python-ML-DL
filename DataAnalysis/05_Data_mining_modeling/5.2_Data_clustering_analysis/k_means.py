# @Project:AID1810
# @Author:biabu
# @Date:19-2-1 下午3:54
# @File_name:k_means.py
# @IDE:PyCharm

"""
采用K-Means聚类分析，对部分餐饮客户的消费行为进行分析，设定聚类数K为3，最大迭代次数500次，距离函数采用欧氏距离
"""

import pandas as pd
from sklearn.cluster import KMeans

# 参数初始化
inputfile = '../data/consumption_data.xls'
outputfile = '../tmp/data_type.xls'

k = 3  # 聚类数为3
iteration = 500  # 最大迭代500次
data = pd.read_excel(inputfile, index_col='Id')  # 读取数据
# 为了消除指标之间的量纲和取值范围差异的影响，用零均值标准化对原始数据进行数据标准化，处理后的数据的均值就是0，标准差为1
data_zs = 1.0 * (data - data.mean()) / data.std()

# 建立聚类模型，分为3类，cpu并发为4，最大迭代500次
model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)
model.fit(data_zs)  # 开始聚类

# 简单打印结果
r1 = pd.Series(model.labels_).value_counts()  # 统计各个类别数目
r2 = pd.DataFrame(model.cluster_centers_)  # 打印聚类中心
# 横向连接(0是纵向)，得到聚类中心对应类别下的数目
r = pd.concat([r2, r1], axis=1)
r.columns = list(data.columns) + ["类目数目"]  # 重命名表头
print(r)

# 详细输出原始数据及其类别
r_detail = pd.concat(
    [data, pd.Series(model.labels_, index=data.index)], axis=1)
r_detail.columns = list(data.columns) + [u'聚类类别']
r_detail.to_excel(outputfile)  # 保存结果


#############################################
# 绘制聚类后的概率密度图

def density_plot1(data, title):
    import matplotlib.pylab as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.figure()
    for i in range(len(data.iloc[0])):  # 逐列作图
        (data.iloc[:, i]).plot(kind='kde', labels=data.columns[i], linewidth=2)
    plt.ylabel("密度")
    plt.xlabel("人数")
    plt.title("聚类类别%s各属性的密度曲线" % title)
    plt.legend()
    return plt


def density_plot(data):
    import matplotlib.pylab as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    p = data.plot(
        kind='kde', linewidth=2,
        subplots=True, sharex=False)
    [p[i].set_ylabel(u'密度') for i in range(k)]
    plt.legend()
    return plt


pic_output = '../tmp/pd_'  # 概率密度图前缀名
for i in range(k):
    data_r = data[r_detail["聚类类别"] == i]
    density_plot(data_r).savefig('%s%s.png' % (pic_output, i))

"""
# 对kmeans结果可视化展示
from sklearn.manifold import TSNE

tsne = TSNE()
# 数据降维
tsne.fit_transform(data_zs)
tsne = pd.DataFrame(tsne.embedding_, index=data_zs.index)


#不同类别用不同颜色和样式绘图
d = tsne[r_detail['聚类类别'] == 0]
plt.plot(d[0], d[1], 'r.')
d = tsne[r_detail['聚类类别'] == 1]
plt.plot(d[0], d[1], 'go')
d = tsne[r_detail['聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*')
plt.show()
"""
