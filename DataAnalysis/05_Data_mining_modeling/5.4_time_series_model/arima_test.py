# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/2/21 9:27
# @File_name:arima_test.py
# @IDE:PyCharm

"""
arima(0,1,1) 时序模式根据某餐厅的2015/1/1/~2015/2/6的销售数据，对2015/2/7 ~ 2015/2/11销售进行预测

模型训练过程中无法收敛
"""


import pandas as pd
import matplotlib.pyplot as plt

# 参数初始化
discfile = '../data/arima_data.xls'
forecastnum = 5
# 读取数据，指定日期列为指标，pandas自动将“日期”列识别为Datetime格式
data = pd.read_excel(discfile, index_col='日期',dtype={'销量': float})


plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 时序图
data.plot()
plt.show()

# 自相关图
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
plot_acf(data).show()

# 平稳性检测
from statsmodels.tsa.stattools import adfuller as ADF
print('原始数据的ADF检验结果为：',ADF(data['销量']))
# 返回值为adf, pvalue,usedlag,nobs,critical values,icbest,regresults,resstore

# 差分后的结果
D_data = data.diff().dropna()
D_data.columns = ['销量差分']
D_data.plot()  # 差分后的时序图
plt.show()
plot_acf(D_data).show()  # 差分后的自相关图
plot_pacf(D_data).show()  # 差分后的偏自相关图
print("差分序列的ADF检验结果为：", ADF(D_data['销量差分']))

# 白噪声检验
from statsmodels.stats.diagnostic import acorr_ljungbox
print("差分序列的白噪声检验为：",acorr_ljungbox(D_data,lags=1))  # 返回统计量和p值


# 模型定阶预测
from statsmodels.tsa.arima_model import ARIMA

# 定阶
pmax = int(len(D_data/10))  # 一般阶数不超过 length/10
qmax = int(len(D_data)/10)

bic_matrix = []  # bic矩阵
for p in range(pmax+1):
    for q in range(qmax+1):
        try:
            bic_matrix.append(ARIMA(data, (p,1,q)).fit().bic)
        except:
            bic_matrix.append(None)


bic_matrix = pd.DataFrame(bic_matrix)  # 可从中找出最小值
print(bic_matrix)
p,q = bic_matrix.stack().idxmin()  # 先用stack展平，用idxmin 找出最小值位置
print('BIC最小的p值和q值为:%s,%s' % (p,q))
model = ARIMA(data, (p,1,q)).fit()  # 建立模型
model.summary2()  # 给出一份模型报告
model.forecast(5)  # 做为期5天的销售预测，返回预测结果、标准误差、置信区间

