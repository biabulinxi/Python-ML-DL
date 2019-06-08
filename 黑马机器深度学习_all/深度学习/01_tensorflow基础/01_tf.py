# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/29 17:06
# @File_name:01_tf.py
# @IDE:PyCharm

import tensorflow as tf
import os

# 关闭tensorflow的警告信息
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# # 创建一幅图包含了一组op和tensor,上下文环境
# # op:只要使用tensorflow的API定义的函数都是OP
# # tensor:指代的是数据
# g = tf.Graph()
# print(g)
# with g.as_default():
#     c = tf.constant(11.0)
#     print(c.graph)
#
# # 实现加法运算
# a = tf.constant(5.0)
# b = tf.constant(6.0)
# print(a, b)
#
# sum1 = tf.add(a, b)
# print(sum1)
#
# # 默认的这张图，相当于给程序分配一段内存
# graph = tf.get_default_graph()
#
# # 不是op不能运行
# var1 = 2
# var2 = 3
# sum2 = var1 + var2
#
# # tf有重载机制,只有和op运算，则会重载成op
# sum3 = var1 + a
# print(sum2)
#
# # 训练模型
# # 实时提供数据进行训练
# # placehodler是一个占位符, feed_dict是一个字典
# plt = tf.placeholder(tf.float32, [None, 3])
# print('plt',plt)
#
# # 会话，一次只能运行一个图结构, 默认系统图
# # 只要有会话的上下文环境，都可以使用eval()
# with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
#     print(sess.run([a, b, sum1, sum3]))
#     print(sess.run(plt, feed_dict={plt: [[1, 2, 3], [4, 5, 6]]}))
#     print('-'*50)
#     print(a.graph)
#     print('-'*50)
#     print(a.shape)
#     print('-'*50)
#     print(a.name)
#     print('-'*50)
#     print(a.op)
#     print('-'*50)
#     print(sum1.graph)
#     print(sess.graph)
#
# with tf.Session(graph=g) as sess:
#     print(c.eval())

# ########################################################
# # tensorflow: 打印的形状表示
# # 0维:(),   1维:(2),    2维：(2,3),     3维:(2,3,4)
#
# # 形状的概念
# # 静态形状好和动态形状
#
# plt = tf.placeholder(tf.float32,[None,2])
# print(plt)
#
# # 设置静态形状
# plt.set_shape([3,2])
# print(plt)
# # 对于静态形状来说，一旦设置成功，则不能在设置静态形状，也不能跨维度修改
# # 但可以用动态形状取创建一个新的形状张量，但元素数量要匹配，可以进行维度修改
# # plt.set_shape([4,2])
# plt_reshape = tf.reshape(plt,[2,3])
# print(plt_reshape)
#
# with tf.Session as sess:
#     pass


#####################################################################
###### 变量op,  变量可以持久化保存，变量必须进行初始化, name 参数在tensorboard 显示名字，区分相同的op

# 变量的创建
a = tf.constant(1,name='a')
b = tf.constant(2,name='b')

c = tf.add(a,b,name='add')

var = tf.Variable(tf.random_normal([2,3],mean=0.0,stddev=1.0),name='variable')
print(a,var)

# 向量初始化
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    # 运行变量初始化OP
    sess.run(init_op)
    print(sess.run([c, var]))

    # 把程序的图结构写入事件文件,graph:把指定的图写入文件当中
    filewriter = tf.summary.FileWriter('C:/Users/Pycharm/AID1810/tensorboard/tmp/summary/test',graph=sess.graph)





