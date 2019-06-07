# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/21 17:14
# @File_name:demo09_interpolate.py
# @IDE:PyCharm

"""
插值
"""

import scipy.interpolate as si
import numpy as np
import matplotlib.pyplot as plt

dis_x = np.linspace(-50,50,13)
dis_y = np.sinc(dis_x)
plt.figure('Interpolate')
plt.title('Interpolate')
plt.grid(linestyle=':')
plt.scatter(dis_x, dis_y,marker='D',c='r',label='points')

# 构建插值器函数
linear = si.interp1d(dis_x,dis_y,kind='linear')
lin_x = np.linspace(-50, 50, 1000)
lin_y = linear(lin_x)
plt.plot(lin_x, lin_y, c='b',label='Linear Interpolate')

# 三次样条插值
cubic = si.interp1d(dis_x,dis_y,kind='cubic')
lin_x = np.linspace(-50, 50, 1000)
lin_y = cubic(lin_x)
plt.plot(lin_x, lin_y, c='g',label='Cubic Interpolate')

# 拉格朗日插值
lagrange = si.lagrange(dis_x,dis_y,)
lin_x = np.linspace(-50, 50, 1000)
lin_y = lagrange(lin_x)
plt.plot(lin_x, lin_y, c='y',label='Lagrange Interpolate')


###############################################
# 牛顿插值
def get_order_diff_quot(xi = [], fi = []):
    """
    @brief:   计算n阶差商 f[x0, x1, x2 ... xn]
    @param:   xi   所有插值节点的横坐标集合                                                        o
    @param:   fi   所有插值节点的纵坐标集合                                                      /   \
    @return:  返回xi的i阶差商(i为xi长度减1)                                                     o     o
    @notice:  a. 必须确保xi与fi长度相等                                                        / \   / \
              b. 由于用到了递归，所以留意不要爆栈了.                                           o   o o   o
              c. 递归减递归(每层递归包含两个递归函数), 每层递归次数呈二次幂增长，总次数是一个满二叉树的所有节点数量(所以极易栈溢出)
    """
    if len(xi) > 2 and len(fi) > 2:
        return (get_order_diff_quot(xi[:len(xi) - 1], fi[:len(fi) - 1]) - get_order_diff_quot(xi[1:len(xi)], fi[1:len(fi)])) / float(xi[0] - xi[-1])
    return (fi[0] - fi[1]) / float(xi[0] - xi[1])


def get_Wi(i = 0, xi = []):
    """
    @brief:  获得Wi(x)函数;
             Wi的含义举例 W1 = (x - x0); W2 = (x - x0)(x - x1); W3 = (x - x0)(x - x1)(x - x2)
    @param:  i  i阶(i次多项式)
    @param:  xi  所有插值节点的横坐标集合
    @return: 返回Wi(x)函数
    """
    def Wi(x):
        result = 1.0
        for each in range(i):
            result *= (x - xi[each])
        return result
    return Wi


def get_Newton_inter(xi = [], fi = []):
    """
    @brief: 获得牛顿插值函数
    @
    """
    def Newton_inter(x):
        result = fi[0]
        for i in range(2, len(xi)):
            result += (get_order_diff_quot(xi[:i], fi[:i]) * get_Wi(i-1, xi)(x))
        return result
    return Newton_inter

newton = get_Newton_inter(list(dis_x),list(dis_y))
nt_x = np.linspace(-50, 50, 1000)
nt_y = newton(nt_x)
plt.plot(nt_x, nt_y, c='b',label='Newton Interpolate')


plt.legend()
plt.show()


