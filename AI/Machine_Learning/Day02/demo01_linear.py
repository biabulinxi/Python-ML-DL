# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/25 17:37
# @File_name:demo01_linear.py
# @IDE:PyCharm

"""
线性回归梯度下降
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as axes3d


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

    # 将梯度下降的过程进行输出
    print('{:4}>>> w0={:.8f}, w0={:.8f}, loss={:.8f}'.format(epoches[-1],w0[-1],w1[-1],losses[-1]))

    # 根据偏导数公式，求w0 和 w1方向上的梯度值
    d0 = ((w0[-1]+w1[-1]*train_x) - train_y).sum()
    d1 = ((w0[-1] + w1[-1] * train_x - train_y)* train_x).sum()
    w0.append(w0[-1] - rate*d0)
    w1.append(w1[-1] - rate*d1)

# 经过1000次梯度下降，最终得到w0 w1是的loss最小
pred_y = w0[-1] + w1[-1]*train_x



# 绘制训练数据,拟合曲线图
plt.figure()
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
plt.scatter(train_x, train_y, marker='o', s=60, c='b', label='Train Points')
plt.plot(train_x,pred_y,c='r',linewidth=2, label='Regression Line')
plt.legend()

# 绘制随着每次梯度下降的过程，w0,w1,loss函数的变化曲线
plt.figure('Training Progress')
plt.subplot(311)
plt.title('Training w0',fontsize=14)
plt.ylabel('w0', fontsize=12)
plt.grid(linestyle=':')
plt.tick_params(labelsize=10)
plt.plot(epoches,w0[:-1],c='b',label='w0 Progress')
plt.legend()

plt.subplot(312)
plt.title('Training w1',fontsize=14)
plt.ylabel('w1', fontsize=12)
plt.grid(linestyle=':')
plt.tick_params(labelsize=10)
plt.plot(epoches,w1[:-1],c='b',label='w1 Progress')
plt.legend()

plt.subplot(313)
plt.title('Training Loss',fontsize=14)
plt.ylabel('loss', fontsize=12)
plt.grid(linestyle=':')
plt.tick_params(labelsize=10)
plt.plot(epoches,losses,c='b',label='Loss Progress')
plt.legend()

#绘制三维梯度下降的过程
grid_w0, grid_w1 = np.meshgrid(np.linspace(0,9,500),np.linspace(0,3.5,500))
grid_loss = np.zeros_like(grid_w0)
for x, y in zip(train_x, train_y):
    grid_loss += (grid_w0 + grid_w1*x - y)**2 /2

plt.figure('Loss Function')
ax3d = plt.gca(projection='3d')
ax3d.set_xlabel('w0',fontsize=14)
ax3d.set_ylabel('w1',fontsize=14)
ax3d.set_zlabel('loss',fontsize=14)
ax3d.plot_surface(grid_w0, grid_w1, grid_loss,rstride=10, cstride=10, cmap='jet')
ax3d.plot(w0[:-1], w1[:-1], losses,'o-', color='orangered')

# 在等高线中绘制梯度下降过程
plt.figure('BGD Countour')
plt.title('BGD Countour')
plt.xlabel('w0',fontsize=12)
plt.xlabel('w1',fontsize=12)
plt.tick_params(labelsize=10)
plt.contourf(grid_w0,grid_w1,grid_loss,10, cmap='jet')
cntr = plt.contour(grid_w0,grid_w1,grid_loss,10, color='black')
plt.clabel(cntr, inline_spacing=0.1, fmt='%.2f')
plt.plot(w0, w1, 'o-', c='orangered',label='BGD')
plt.legend()

plt.tight_layout()
plt.show()
