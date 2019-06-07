# -*- coding: utf-8 -*-

"""
apriori 算法的函数文件
"""


import pandas as pd


# 自定义连接函数，用于实现L_{k-1}到C_k的连接
def connect_string(C_k, ms):
    """
    aprior算法的连接函数，用来连接各个频繁项集
    :param C_k: 初步筛选的数据项集
    :param ms: 数据项集用 ==> 进行连接
    :return:
    """
    C_k = list(map(lambda i: sorted(i.split(ms)), C_k))  # 将初步筛选的数据项集用没事拆分后进行排序, 放入列表中
    print(C_k)
    l = len(C_k[0])  # 取第一列数据的长度，而其只有一列
    r = []  # 将 C_k 中的每一个元素，与其后的元素进行遍历连接，得到候选集项 C_k
    for i in range(len(C_k)):
        for j in range(i, len(C_k)):
            if C_k[i][:l - 1] == C_k[j][:l - 1] and C_k[i][l - 1] != C_k[j][l - 1]:
                r.append(C_k[i][:l - 1] + sorted([C_k[j][l - 1], C_k[i][l - 1]]))
    return r


# 寻找关联规则的函数
def find_rule(d, support, confidence, ms=u'==>'):
    """
    寻找关联规则的函数
    :param d: 处理过的 0-1 数据集
    :param support: 最小支持度
    :param confidence: 最小置信度
    :param ms: 连接符
    :return: 最强关联规则
    """

    result = pd.DataFrame(index=['support', 'confidence'])  # 定义输出结果

    support_series = 1.0 * d.sum() / len(d)  # 支持度序列：d.sum()将每一个序列进行求和，最后除以总事件数

    column = list(support_series[support_series > support].index)  # 初步根据支持度筛选，将筛选过的元素索引添加进列表中


    k = 0  # 计数器
    while len(column) > 1:
        k = k + 1
        print(u'\n正在进行第%s次搜索...' % k)
        column = connect_string(column, ms)  # 将有关联的数据项集用 ==> 进行连接
        print(u'数目：%s...' % len(column))
        sf = lambda i: d[i].prod(axis=1, numeric_only=True)  # 新一批支持度的计算函数, 返回请求列的值的乘积

        # 创建连接数据，这一步耗时、耗内存最严重。当数据集较大时，可以考虑并行运算优化。
        d_2 = pd.DataFrame(list(map(sf, column)), index=[ms.join(i) for i in column]).T

        support_series_2 = 1.0 * d_2[[ms.join(i) for i in column]].sum() / len(d)  # 计算连接后的支持度
        column = list(support_series_2[support_series_2 > support].index)  # 新一轮支持度筛选
        support_series = support_series.append(support_series_2)
        column2 = []

        for i in column:  # 遍历可能的推理，如{A,B,C}究竟是A+B-->C还是B+C-->A还是C+A-->B？
            i = i.split(ms)
            for j in range(len(i)):
                column2.append(i[:j] + i[j + 1:] + i[j:j + 1])

        cofidence_series = pd.Series(index=[ms.join(i) for i in column2])  # 定义置信度序列

        for i in column2:  # 计算置信度序列
            cofidence_series[ms.join(i)] = support_series[ms.join(sorted(i))] / support_series[ms.join(i[:len(i) - 1])]

        for i in cofidence_series[cofidence_series > confidence].index:  # 置信度筛选
            result[i] = 0.0
            result[i]['confidence'] = cofidence_series[i]
            result[i]['support'] = support_series[ms.join(sorted(i.split(ms)))]

    # result = result.T(['confidence', 'support'])  # 结果整理，输出
    result = result.T.sort_index() # 结果整理，输出

    print(u'\n结果为：')
    print(result)

    return result
