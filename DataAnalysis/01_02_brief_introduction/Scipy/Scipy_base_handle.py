# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/23 19:49
# @File_name:Scipy_base_handle.py
# @IDE:PyCharm

"""求解非线性方程组2X1-X2^2=1, x1^2-x2=2"""
from scipy.optimize import fsolve  # 导入求解分线性方程组的函数 fsolv


# 定义要求的方程组
def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2 * x1 - x2 ** 2 - 1, x1 ** 2 - x2 - 2]


result = fsolve(f, [1, 1])  # 输入初始值x1=1,x2=1进行求解
print(result)  # 输出结果


"""数值积分"""
from scipy import integrate  # 导入积分函数 integrate


# 定义积分函数
def g(x):
    return (1-x**2)**0.5


pi_2, err = integrate.quad(g, -1, 1)  # x在(-1,1)区间内的积分结果和误差
print(pi_2*2)  # 积分结果为圆周率的一半










