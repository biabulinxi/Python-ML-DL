# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/31 15:53
# @File_name:neural_network.py
# @IDE:PyCharm

"""
使用使用神经网络算法预测销量高低, 建立的神经网络有3个输入节点，10个隐藏节点，1个输出节点
"""

import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from sklearn.metrics import confusion_matrix  # 导入混淆矩阵函数
from cm_plot import *

# 初始化参数，读入数据
filename = '../data/sales_data.xls'
data = pd.read_excel(filename, index_col="序号")

# 将数据类别进行编码转化成数字
# 用1来表示“好”“是”“高”，0表示“坏”“否”“低”
data[data == '好'] = 1
data[data == '是'] = 1
data[data == '高'] = 1
data[data != 1] = 0
x = data.iloc[:, :3].as_matrix().astype(int)
y = data.iloc[:, 3].as_matrix().astype(int)

# 建立神经网络模型
model = Sequential()
model.add(Dense(3))
model.add(Dense(units=10, activation='relu'))  # 用rule函数作为隐藏层的激活函数，大幅提高准确度
model.add(Dense(1, activation='sigmoid'))  # 由于是0-1输出，用sigmoid作为激活函数

"""
编译模型，因为做的时二元分类，所以指定损失函数为binary_corrssentropy(二元交叉熵)，模式为binary
另外还有常见的损失函数有：mean_squared_error(均方误差), categorical_crossentropy(绝对交叉熵)等
求解方法选用adam，还有sgd, rmsprop等
"""
model.compile(loss='binary_crossentropy', optimizer='adam', class_mode='binary')

model.fit(x, y, nb_epoch=1000, batch_size=10)  # 训练模型，学习1000次
yp = model.predict_classes(x).reshape(len(y))  # 分类预测

# 显示混淆矩阵可视化结果
cm_plot(y, yp).show()

