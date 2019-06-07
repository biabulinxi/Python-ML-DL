# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/28 10:11
# @File_name:01_statistics_analysis.py
# @IDE:PyCharm

"""餐饮数据统计量分析"""
import pandas as pd

catering_sale = "../data/catering_sale.xls"
data = pd.read_excel(catering_sale, index_col="日期")
# 根据数据质量分析中的箱线图分析，过滤异常数据
data = data[(data["销量"] > 400) & (data["销量"] < 5000)]
# 保存基本统计量
statistics = data.describe()

# 求极差
statistics.loc["range"] = statistics.loc['max'] - statistics.loc["min"]
# 变异系数
statistics.loc["var"] = statistics.loc["std"] / statistics.loc["mean"]
# 四分位数间距
statistics.loc["dis"] = statistics.loc["75%"] - statistics.loc["25%"]

print(statistics)
