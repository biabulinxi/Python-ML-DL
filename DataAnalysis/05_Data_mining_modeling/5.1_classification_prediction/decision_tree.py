# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/31 10:00
# @File_name:decision_tree.py
# @IDE:PyCharm

"""
使用ID3决策树算法预测销量高低
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC  # 导入决策树分类器
from sklearn.tree import export_graphviz  # 导出决策树

# 初始化参数，读入数据
filename = '../data/sales_data.xls'
data = pd.read_excel(filename, index_col="序号")

# 将数据类别进行编码转化成数字
# 用1来表示“好”“是”“高”，-1表示“坏”“否”“低”
data[data == '好'] = 1
data[data == '是'] = 1
data[data == '高'] = 1
data[data != 1] = -1
x = data.iloc[:, :3].astype(int)
y = data.iloc[:, 3].astype(int)

# 建立基于信息熵的决策树模型
dtc = DTC(criterion='entropy')
dtc.fit(x, y)  # 训练模型

# 可视化决策树，导出结果为dot文件，需安装Graphviz将其转换为pdf或jpg格式
with open('../tmp/tree.dot', 'w') as f:
    f = export_graphviz(dtc, feature_names=x.columns, out_file=f)
