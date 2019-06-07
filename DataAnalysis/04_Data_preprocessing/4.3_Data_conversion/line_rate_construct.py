# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/30 9:15
# @File_name:line_rate_construct.py
# @IDE:PyCharm

"""
在防窃漏电中，为了方便更清楚的检测用户窃漏电行为，构造线损率属性，线损率正常范围在3%~15%
线损率=（供入电量-供出电量）/供出电量 x 100%
"""

import pandas as pd

inputfile = '../data/electricity_data.xls'  # 原始数据
outputfile = '../tmp/electricity_data.xls'  # 构造属性后的数据文件

data = pd.read_excel(inputfile)
data["线损率"] = (data["供入电量"] - data["供出电量"])/data['供入电量']

data.to_excel(outputfile, index=False)  # index=False 输出不保存索引序号
print("写入成功")

