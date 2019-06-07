# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/21 9:50
# @File_name:demo02_eig.py
# @IDE:PyCharm

"""
提取图片的特征值
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

# 绘制图片
plt.figure('蔡文静',facecolor='lightgray')

plt.subplot(1,2,1)
plt.xticks([])    # 取消刻度
plt.yticks([])
plt.imshow(image, cmap='gray')  # 灰度映射
plt.tight_layout()  # 适应窗口
plt.subplot(1,2,2)
plt.xticks([])    # 取消刻度
plt.yticks([])
plt.imshow(S, cmap='gray')  # 灰度映射
plt.tight_layout()  # 适应窗口

plt.show()