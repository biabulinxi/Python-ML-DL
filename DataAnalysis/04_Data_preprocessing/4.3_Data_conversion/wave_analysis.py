# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/30 9:58
# @File_name:wave_analysis.py
# @IDE:PyCharm

"""
利用小波函数对声波信号数据进行分解，得到5个层次的小波系数，利用这些小波系数求得各个能量值，
这些能量值可作为声波信号的特征数据
"""

from scipy.io import loadmat  # 导入loadmat函数，读取MATLAB的信号文件
import pywt   # PyWavelets 是一个较好的信号处理库

inputfile = "../data/leleccum.mat"
mat = loadmat(inputfile)
signal = mat['leleccum'][0]
# 返回结果为level+1个数组，每个数组为一个系数，第一个数组为逼近系数数组，后面的依次是细节系数数组，wavedec 数据的多级一维离散小波变换，bior3.7 是一种双正交小波函数

coeffs = pywt.wavedec(signal, 'bior3.7', level=5)
print(coeffs)
