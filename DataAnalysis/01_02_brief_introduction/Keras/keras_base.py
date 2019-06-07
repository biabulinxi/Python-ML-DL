# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/25 9:19
# @File_name:keras_base.py
# @IDE:PyCharm

"""利用 Keras 搭建一个 MLP 多层感知器"""

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD

# 模型初始化，创建一个连续模型
model = Sequential()
# 添加输入层(20个节点)、第一隐藏层(64节点)的连接
model.add(Dense(20,64))
# 第一隐藏层用 tanh 作为激活函数
model.add(Activation('tanh'))
# 使用 Dropout 防止过拟合
model.add(Dropout(0.5))
# 添加第一隐藏层，第二隐藏层(64节点)的连接
model.add(Dense(64, 64))
# 第二隐藏层用 tanh 作为激活函数
model.add(Activation('tanh'))
# 使用 Dropout 防止过拟合
model.add(Dropout(0.5))
# 添加第二隐藏层(64节点)，输出层(1节点)
model.add(Dense(64, 1))
# 输出层用 sigmoid 作为激活函数
model.add(Activation('sigmoid'))

# 定义求解算法
sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
# 编译生成模型，损失函数为平均误差平方和
model.compile(loss='mean_squared_error', optimizer=sgd)

# 训练模型
model.fit(X_train, y_train, nb_epoch=20, batch_size=16)
# 测试模型
score = model.evaluate(X_test, y_test, batch_size=16)
