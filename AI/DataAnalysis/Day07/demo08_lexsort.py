# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/21 16:11
# @File_name:demo08_lexsort.py
# @IDE:PyCharm

"""
案例：为商品排序，先价格，后销量
"""

import numpy as np

goods = np.array(['苹果','华为','OPPO','MI','VIVO'])
prices = np.array([8888,4500,3999,2999,3999])
sales = np.array([99,200,99,110,80,])

# 联合间接排序,默认升序
indices = np.lexsort((sales, prices))
print(goods[indices])

# 插入排序

a = np.array([1,2,4,6,8])
b = np.array([3,5])
indexs = np.searchsorted(a, b)
a = np.insert(a,indexs,b)
print(indexs)
print(a)