# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/26 14:40
# @File_name:demo05_ridge.py
# @IDE:PyCharm

import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import sklearn.metrics as sm

x, y = np.loadtxt('../ml_data/abnormal.txt',delimiter=',',usecols=(0,1), unpack=True)


x = x.reshape(-1, 1)  # x变为n行1列

# 线性回归模型
model = lm.LinearRegression()
model.fit(x, y)
pred_y = model.predict(x)

# 岭回归模型
r_model = lm.Ridge(150,fit_intercept=True,max_iter=1000)
r_model.fit(x, y)
r_pred_y = r_model.predict(x)

#####################################################
# 评估模型的误差
# 平均绝对值误差：1/m*∑|实际输出-预测输出|
print(sm.mean_absolute_error(y,pred_y))
print(sm.mean_absolute_error(y,r_pred_y))
# 平均平方误差：sqrt(1/m*∑(实际输出-预测输出)^2)
print(sm.mean_squared_error(y, pred_y))
print(sm.mean_squared_error(y, r_pred_y))
# 中位数绝对值误差: median(|实际输出-预测输出|)
print(sm.median_absolute_error(y, pred_y))
print(sm.median_absolute_error(y, r_pred_y))
# R2得分 (0, 1]区间上的分值，分数越高，模型越好, 误差越小
print(sm.r2_score(y,pred_y))
print(sm.r2_score(y,r_pred_y))

plt.figure('Linear Regression', facecolor='lightgray')
plt.title('Linear Regression', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(linestyle=":")
plt.scatter(x, y, c='dodgerblue', alpha=0.5,s=60, label='Sample Points')
plt.plot(x, pred_y, c='orangered',linewidth=2,label='Regression Line')
plt.plot(x, r_pred_y, c='b',linewidth=2,label='Ridge  Regression Line')

plt.legend()
plt.show()

