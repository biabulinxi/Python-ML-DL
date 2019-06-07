#-*- coding: utf-8 -*-
#使用Apriori算法挖掘菜品订单关联规则

import pandas as pd
from apriori import * #导入自行编写的apriori函数

inputfile = '../data/menu_orders.xls'
outputfile = '../tmp/apriori_rules.xls' #结果文件
data = pd.read_excel(inputfile, header = None)
print(data)

print('\n转换原始数据至0-1矩阵...')
ct = lambda x : pd.Series(1, index = x[pd.notnull(x)]) #转换0-1矩阵的过渡函数,筛选出数据中的a,b,c,d,e项，并转换为1
b = map(ct, data.as_matrix()) #用map方式执行,

data = pd.DataFrame(list(b)).fillna(0) #实现矩阵转换，空值用0填充
print('转换完毕:\n',data)
del b #删除中间变量b，节省内存

support = 0.2 #定义最小支持度
confidence = 0.5 #定义最小置信度
ms = '==>' #连接符，默认'==>'，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符

find_rule(data, support, confidence, ms).to_excel(outputfile) #保存结果