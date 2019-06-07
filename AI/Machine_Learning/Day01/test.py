# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/25 18:09
# @File_name:test.py
# @IDE:PyCharm

from sympy import symbols, diff
import numpy as np
import matplotlib.pyplot as plt

train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])

def test_diff():
    global train_x, train_y
    w0, w1 = symbols('w0 w1')
    loss = (((w0 + w1 * train_x - train_y)) ** 2).sum() / 2
    d_0 = diff(loss, w0)
    d_1 = diff(loss, w0)
    return d_0,d_1

times = 1000  # 步数
rate = 0.01  # 步长
epoches = []  # 记录每次梯度下降的索引
w0, w1, losses = [1], [1], []  # 初始化数据
d = {
    'w0':w0[-1],
    'w1':w1[-1],
}
# 模拟梯度下降
for i in range(1, times + 1):
    d_0, d_1 = test_diff()
    d0 = d_0.subs(d).evalf()
    d1 = d_1.subs(d).evalf()
    w0.append(w0[-1] - rate * d0)
    w1.append(w1[-1] - rate * d1)

print(w0, w1)
pred_y = w0[-1] + w1[-1]*train_x
print(pred_y)
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