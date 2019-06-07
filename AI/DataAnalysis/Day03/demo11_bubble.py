# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/15 15:56
# @File_name:demo11_bubble.py
# @IDE:PyCharm

"""
案例：随机生成各种颜色的100个气泡，让他们不断能增大，最后破裂，重新开始
1. 随机生成100个气泡
2. 每个气泡拥有四个属性：position，size， growth, color
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ma

n = 100
balls = np.zeros(n, dtype=[
    ('position', float, 2),  # 位置属性
    ('size', float, 1),  # 大小
    ('growth', float, 1),  # 生长速度
    ('color', float, 4),  # 颜色属性
])

# 初始化属性
# uniform(0, 1, (n,2)) : 从0到1取随机数，填充n行2列的数组
balls['position'] = np.random.uniform(0, 1, (n, 2))
balls['size'] = np.random.uniform(50, 70, n)
balls['growth'] = np.random.uniform(10, 20, n)
balls['color'] = np.random.uniform(0, 1, (n, 4))

# 绘制100个散点泡泡
plt.figure('Bubble', facecolor='lightgray')
plt.title("Bubble", fontsize=18)
plt.xticks([])
plt.yticks([])
sc = plt.scatter(
    balls['position'][:, 0],
    balls['position'][:, 1],
    balls['size'],
    color=balls['color'],
)


# 启动动画
def update(number):
    balls['size'] += balls['growth']
    # 设置破裂阈值
    boom_i = number % n
    balls[boom_i]['size'] = 60
    balls[boom_i]['position'] = np.random.uniform(0, 1, (1, 2))
    # 重新设置属性
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])


anim = ma.FuncAnimation(plt.gcf(), update, interval=30)
plt.show()
