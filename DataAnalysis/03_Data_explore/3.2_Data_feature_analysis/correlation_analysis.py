# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/28 14:09
# @File_name:correlation_analysis.py
# @IDE:PyCharm

"""餐饮销售数据相关性分析"""
import pandas as pd

catering_sale = "../data/catering_sale_all.xls"   # 导入餐饮销售数据，含有其他属性
data = pd.read_excel(catering_sale, index_col="日期")  # 读取数据，指定“日期”为索引列

# 调用相关系数矩阵，即给出任意两款菜式之间的相关系数
print(data.corr())
# 只显示"百合酱蒸凤爪"与其他菜式之间的相关系数
print(data.corr()["百合酱蒸凤爪"])
# 只显示"百合酱蒸凤爪"与"百合酱蒸凤爪"的相关系数
print(data["百合酱蒸凤爪"].corr(data["百合酱蒸凤爪"]))