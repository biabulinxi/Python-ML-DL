# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/21 17:44
# @File_name:demo10_ndimage.py
# @IDE:PyCharm

"""
图像处理
"""

import numpy as np
import matplotlib.pyplot as mp
import scipy.misc as sm
import scipy.ndimage as sn

image = sm.imread('./蔡文静.jpg',True)

# 高斯模糊
image2 = sn.median_filter(image, 20)
# 角度旋转
image3 = sn.rotate(image, 45)
# 边沿识别
image4 = sn.prewitt(image)

mp.figure()
mp.subplot(221)
mp.imshow(image,cmap='gray')
mp.axis('off')

mp.subplot(222)
mp.imshow(image2,cmap='gray')
mp.axis('off')

mp.subplot(223)
mp.imshow(image3,cmap='gray')
mp.axis('off')

mp.subplot(224)
mp.imshow(image4,cmap='gray')
mp.axis('off')

mp.show()
