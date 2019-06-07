# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/23 20:09
# @File_name:matplotlib_base_handle.py
# @IDE:PyCharm

import numpy as np
import matplotlib.pyplot as plt  # 导入matplotlib

x = np.linspace(0, 10, 1000)  # 自变量 x=(0,10),总共设置1000个点进行曲线圆滑优化
y = np.sin(x) + 1  # 因变量 y
z = np.cos(x**2) + 1  # 因变量 z

plt.figure(figsize = (8, 4))
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体为黑体，可显示中文标签
plt.rcParams["axes.unicode_minus"] = False   # 姐姐保存图像负号 - 显示为方块的问题
# 作图,设置标签,线条类型,线条颜色,线条大小
plt.plot(x, y,label = "$\sin x+1$", color = "red", linewidth = 2)
plt.plot(x, z, "b--",label = "$\cos x^2+1$")  # 作图,设置标签,线条类型
plt.xlabel("Time(s)")  # x 轴名称
plt.ylabel("Volt")  # y 轴名称
plt.title("A Simple Example")  # 标题
plt.ylim(0, 2.2)  # 显示 y 轴的坐标范围
plt.legend()  # 显示图例
plt.show()  # 显示作图结果
