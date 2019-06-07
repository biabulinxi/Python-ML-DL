# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/21 9:47
# @File_name:demo01_eig.py
# @IDE:PyCharm

"""
特征值特征向量
"""
import numpy as np

A = np.mat('1 6 5; 9 7 3; 1 5 6')
print(A)
# 特征值提取
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals, eigvecs, sep='\n')
# 通过特征值与特征向量， 求方阵
S = np.mat(eigvecs) * np.mat(np.diag(eigvals)) * np.mat(eigvecs).I
print(S)

eigvals[1:] = 0
S = np.mat(eigvecs) * np.mat(np.diag(eigvals)) * np.mat(eigvecs).I
print(S)
