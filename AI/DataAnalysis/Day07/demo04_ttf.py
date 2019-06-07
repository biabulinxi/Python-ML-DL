# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/21 11:38
# @File_name:demo04_ttf.py
# @IDE:PyCharm

"""
案例：基于傅里叶变换，拆解方波
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 1000)

y1 = 4*np.pi * np.sin(x)
y2 = 4/3*np.pi * np.sin(3*x)
y3 = 4/5*np.pi * np.sin(5*x)

# 叠加1000个波形
n = 1000
y = 0
for i in range(1, n + 1):
    y += 4 * np.pi / (2 * i - 1) * np.sin((2 * i - 1) * x)

#####################################################
# 对y傅里叶变换，拆解方波，绘制频域图像
# 获得复数数组
ffts = np.fft.fft(y)
# 获取傅里叶变换的频率数组
freqs = np.fft.fftfreq(x.size,x[1]-x[0])
pows = np.abs(ffts)
print(freqs.shape)

# 绘制图像
plt.figure('FFT')

plt.subplot(121)
plt.grid(linestyle=':')
plt.plot(x, y, color='r', linewidth=2)
plt.subplot(122)
plt.grid(linestyle=':')
plt.plot(freqs[freqs>0], pows[freqs>0], color='b', linewidth=2)

# 通过傅里叶逆变换，得到原函数
y2 = np.fft.ifft(ffts)
plt.subplot(121)
plt.grid(linestyle=':')
plt.plot(x, y2, color='b', linewidth=7, alpha=0.3)

plt.show()
