# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/25 17:37
# @File_name:demo07_linear.py
# @IDE:PyCharm

"""
线性回归梯度下降
"""

import numpy as np
import matplotlib.pyplot as plt


train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])
test_x = np.array([0.45, 0.55, 1.0, 1.3, 1.5])
test_y = np.array([4.8, 5.3, 6.4, 6.9, 7.3])

times = 1000  # 步数
rate = 0.01  # 步长
epoches = []  # 记录每次梯度下降的索引
w0, w1, losses = [1], [1], []  # 初始化数据

# 模拟梯度下降
for i in range(1, times + 1):
    epoches.append(i)
    loss = (((w0[-1] + w1[-1] * train_x - train_y)) ** 2).sum() / 2
    losses.append(loss)


    # 根据偏导数公式，求w0 和 w1方向上的梯度值
    d0 = ((w0[-1]+w1[-1]*train_x) - train_y).sum()
    d1 = ((w0[-1] + w1[-1] * train_x - train_y)* train_x).sum()
    w0.append(w0[-1] - rate*d0)
    w1.append(w1[-1] - rate*d1)

# 经过1000次梯度下降，最终得到w0 w1是的loss最小
pred_y = w0[-1] + w1[-1]*train_x



# 绘制训练数据
plt.figure()
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
plt.scatter(train_x, train_y, marker='o', s=60, c='b', label='Train Points')
plt.plot(train_x,pred_y,c='r',linewidth=2, label='Regression Line')
plt.legend()
plt.show()
