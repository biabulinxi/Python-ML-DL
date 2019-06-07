# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/21 10:40
# @File_name:demo03_svd.py
# @IDE:PyCharm


"""
提取图片的特征值,奇异值分解
"""

import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as plt

image = sm.imread('蔡文静.jpg', True)  # True只获取像素值
print(type(image), image.shape)

# 提取image矩阵的特征是和特征向量
eigvals, eigvecs = np.linalg.eig(image)
# 抹掉一部分特征值，重新生成图片
print(eigvals.shape)
eigvals[50:] = 0
S = np.mat(eigvecs) * np.mat(np.diag(eigvals)) * np.mat(eigvecs).I
S = S.real

######################################################
# 奇异值分解:矩阵不一定为方阵
U, s, V = np.linalg.svd(image)
print(s.shape)
S2 = np.mat(U) * np.mat(np.diag(s)) * np.mat(V)
# 抹掉一部分奇异值，重新生成图片
s[50:] = 0
S3 = np.mat(U) * np.mat(np.diag(s)) * np.mat(V)

######################################################
# 绘制图片
plt.figure('蔡文静',facecolor='lightgray')

plt.subplot(2,2,1)
plt.xticks([])    # 取消刻度
plt.yticks([])
plt.imshow(image, cmap='gray')  # 灰度映射

plt.subplot(2,2,2)
plt.xticks([])    # 取消刻度
plt.yticks([])
plt.imshow(S, cmap='gray')  # 灰度映射

plt.subplot(2,2,3)
plt.xticks([])    # 取消刻度
plt.yticks([])
plt.imshow(S2, cmap='gray')  # 灰度映射

plt.subplot(2,2,4)
plt.xticks([])    # 取消刻度
plt.yticks([])
plt.imshow(S3, cmap='gray')  # 灰度映射

plt.tight_layout()
plt.show()