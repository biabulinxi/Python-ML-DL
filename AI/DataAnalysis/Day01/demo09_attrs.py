# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/13 17:34
# @File_name:demo09_attrs.py
# @IDE:PyCharm

"""
测试常用属性
"""

import numpy as np

data = np.array([
        [1+9j,2+8j,3+7j],
        [4+6j,5+5j,6+4j],
        [7+3j,8+2j,9+1j],
    ])
print("数据类型", data.dtype)
print("维度", data.ndim)
print("元素所占字节数", data.itemsize)
print("数组所占总字节数", data.nbytes)
print("实部", data.real)
print("虚部", data.imag)
print("转置", data.T)

# 扁平迭代器,抻平后进行返回迭代
for item in data.flat:
    print(item, end=' ')
    print(item.dtype)
