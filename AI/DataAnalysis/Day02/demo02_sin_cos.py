# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/14 9:55
# @File_name:demo02_sin_cos.py
# @IDE:PyCharm

"""
绘制正余弦
"""
import numpy as np
import matplotlib.pyplot as plt

# 绘制正余弦
# 从-π ~ π拆1000个点
x = np.linspace(-np.pi, np.pi, 1000)
sinx = np.sin(x)
cosx = np.cos(x)

# 设置线型，线宽，颜色，透明度, 标签
plt.plot(x, sinx, linestyle='--', linewidth=2, color='b', alpha=0.5, label=r'$y=sin(x)$')
plt.plot(x, cosx, linestyle=':', linewidth=2, color=(0.3, 0.5, 1), alpha=0.5, label=r'$y=cos(x)$')

# 设置坐标的可视范围
# plt.xlim(0, np.pi)
# plt.ylim(0, 1)

# 修改坐标刻度
x_val_list = [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi]
x_text_list = ['-π', r'$-\frac{\pi}{2}$', '0', 'π/2', 'π']
plt.xticks(x_val_list, x_text_list)
y_val_list = [-1, -0.5, 0.5, 1]
y_text_list = ['-1', '-0.5', '0.5', '1']
plt.yticks(y_val_list, y_text_list)

# 设置坐标轴
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# 绘制特殊点
plt.scatter(
    [np.pi/2, np.pi/2],
    [0, 1],
    marker='x', s=80, edgecolors='dodgerblue', facecolor='deepskyblue',zorder=3
)

# 绘制点备注
plt.annotate(
    r'$[\frac{\pi}{2},1]$',          # 备注文本内容
    xycoords='data',     # 目标点的参考坐标系
    xy=(np.pi/2, 1),     # 目标点坐标
    textcoords = 'offset points',   # 备注文本坐标系
    xytext=(20,10),                 # 备注文本坐标
    fontsize=12,                    # 字体
    arrowprops=dict(
        arrowstyle='->',              # 箭头样式
        connectionstyle='angle3',     # 连接样式
    )
)

plt.annotate(
    r'$[\frac{\pi}{2},0]$',          # 备注文本内容
    xycoords='data',     # 目标点的参考坐标系
    xy=(np.pi/2, 0),     # 目标点坐标
    textcoords = 'offset points',   # 备注文本坐标系
    xytext=(-50,-50),                 # 备注文本坐标
    fontsize=12,                    # 字体
    arrowprops=dict(
        arrowstyle='->',              # 箭头样式
        connectionstyle='angle3',     # 连接样式
    )
)


# 显示图例, loc：图例显示位置
plt.legend(loc='best')
plt.show()
