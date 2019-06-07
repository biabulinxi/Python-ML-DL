# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/21 14:16
# @File_name:demo05_vioce_process.py
# @IDE:PyCharm

"""
案例：基于傅里叶变换为音频文件去除噪声。
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wf
import numpy.fft as nf

#####################################################
# 1. 读取音频文件，获取音频文件的基本信息：采样个数、采样周期，每个采样声音的信号值。绘制音频时域：时间、位移图像。

# 获取采样率，采样位移(2^15倍)
sample_rate, noised_sigs = wf.read('../da_data/noised.wav')
print(sample_rate, noised_sigs.shape)

# 采样时间
times = np.arange(len(noised_sigs)) / sample_rate

# 绘制音频时域：时间、位移图像。
plt.figure('Filter',facecolor='lightgray')
plt.subplot(221)
plt.title('Time Domain',fontsize=16)
plt.xlabel('Time(s)', fontsize=12)
plt.ylabel('Signal', fontsize=12)
plt.tick_params(labelsize=8)
plt.grid(linestyle=':')
plt.plot(times[:180], noised_sigs[:180], c='b',label='Noised Sigs',alpha=0.5)
plt.legend()

######################################################
# 2. 基于傅里叶变换，获取音频频域信息，绘制频域：频率、能量图像。
# 获得频率数组
freqs = nf.fftfreq(times.size,times[1]-times[0])
# 获取振幅
noised_ffts = nf.fft(noised_sigs)
noised_pows = np.abs(noised_ffts)

# 绘制频域：频率、能量图像。
plt.subplot(222)
plt.title('Frequency Domain', fontsize=16)
plt.xlabel('freq', fontsize=12)
plt.ylabel('log(Power)', fontsize=12)
plt.tick_params(labelsize=8)
plt.grid(linestyle=':')
plt.semilogy(freqs[freqs>0], noised_pows[freqs>0], c='r',label='Noised Freq')
plt.legend()

#######################################################
# 3. 将低频噪声去除后, 绘制音频频域：频率、能量图像。
# 获取能量最大值坐标
fund_freq = freqs[noised_pows.argmax()]
# 获取所有不大于最大值的信号下标
noised_index = np.where(freqs != fund_freq)
# 将低频信号置0，进行过滤
filter_ffts = noised_ffts.copy()
filter_ffts[noised_index] = 0
filter_pows = np.abs(filter_ffts)
# 绘制过滤后的音频频域：频率、能量图像。
plt.subplot(224)
plt.title('Frequency Domain', fontsize=16)
plt.xlabel('freq', fontsize=12)
plt.ylabel('log(Power)', fontsize=12)
plt.tick_params(labelsize=8)
plt.grid(linestyle=':')
plt.plot(freqs[freqs>0], filter_pows[freqs>0], c='r',label='Filter signal')
plt.legend()

#####################################################
# 4. 基于逆向傅里叶变换，生成新的音频信号，绘制音频时域的：时间、位移图像。
# 傅里叶逆变换
filter_sigs = nf.ifft(filter_ffts)
# 制音频时域的：时间、位移图像。
plt.figure('Filter',facecolor='lightgray')
plt.subplot(223)
plt.title('Time Domain',fontsize=16)
plt.xlabel('Time(s)', fontsize=12)
plt.ylabel('Signal', fontsize=12)
plt.tick_params(labelsize=8)
plt.grid(linestyle=':')
plt.plot(times[:180], filter_sigs[:180], c='b',label='Fliter Sigs',alpha=0.5)
plt.legend()

# 重新生成音频文件
wf.write('../da_data/filter.wav', sample_rate,(filter_sigs * 2**15).astype(np.int16))

plt.tight_layout()
plt.show()

