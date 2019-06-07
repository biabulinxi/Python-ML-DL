# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/13 11:58
# @File_name:demo04_ctype.py
# @IDE:PyCharm

"""
测试自定义的复合类型
"""

import numpy as np

data = [
    ('张三', [90, 80, 70], 15),
    ('李四', [89, 79, 69], 16),
    ('王五', [22, 11, 34], 17),
]

####################################################
# 第一种设置type属性的方式
# U3:     3个Unicode字符，
# 3int32: 3个int32整数（列表）
# int32:  1个int32整数
ary1 = np.array(data, dtype='U3, 3int32, int32')
print(ary1, ary1.shape)
# 获取第三个用户的姓名  'f0': 第一个字段
print(ary1[2]['f0'])

###################################################
# 第二种设置dtype属性的方式
# 列表元组方式指定，[(别名，类型，格式)]
b = np.array(data, dtype=[
    ('name', 'str_', 2),
    ('scores', 'int32', 3),
    ('age', 'int32', 1),
])
print(b)
print(b[1]['scores'][0])

###################################################
# 第三种设置dtype的方式
# 字典列表形式指定：{’name‘:[别名列表]，’formats‘:[格式列表]}
c = np.array(data, dtype={
    'names': ['name', 'scores', 'age'],
    'formats': ['U3', '3int32', 'int32'],
})
print(c)
print(c[1]['age'])

#####################################################
# 第四中设置dtype的方式
# 字典元组指定，{’别名‘：('类型'，存储时的字节偏移量)}
d = np.array(data, dtype={
    'name': ('U3', 0),
    'scores': ('3int32', 16),
    'age': ('int32', 28),
})
print(d)

#####################################################
# ndarray 数组存放日期格式数据
f = np.array(['2011', '2012-01-01', '2013-11-11 11:11:11', '2013-01-01'])
print(f)
# datetime64[D] ：描述时间(精确到day),Y:年，M:月，D:日，h:时，m:分，s:秒
g = f.astype('M8[h]')
print(g, g.dtype)
print(g[3]-g[1])
print(g.astype('int32'))
