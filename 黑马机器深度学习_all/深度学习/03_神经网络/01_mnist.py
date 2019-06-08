# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/2 15:05
# @File_name:01_mnist.py
# @IDE:PyCharm

import tensorflow as tf
from tensorflow.contrib.slim.python.slim.nets.inception_v3 import inception_v3_base
from tensorflow.examples.tutorials.mnist import input_data



# 定义命令行参数
FLAGS = tf.app.flags.FLAGS
tf.flags.DEFINE_integer('is_train', 1, '指定程序是预测还是训练')


def full_connectes():
    # 获取真实数据
    mnist = input_data.read_data_sets('./data/mnist/', one_hot=True)

    # 1.建立数据的占位符，x=[None,784], y=[None,10]
    with tf.variable_scope('data'):
        x = tf.placeholder(tf.float32, [None, 784])
        y_true = tf.placeholder(tf.int32, [None, 10])

    # 2.建立一个全连接层的神经网络，w=[784,10], b=[10]
    with tf.variable_scope('fc_model'):
        # 随机初始化权重和偏置
        weight = tf.Variable(tf.random_normal([784, 10], mean=0.0, stddev=1.0), name='w')
        bias = tf.Variable(tf.zeros([10], name='b'))

        # 预测None个样本的输出结果[None,784] * [784,10] + [10] = [None, 10]
        y_predict = tf.matmul(x, weight) + bias

    # 3.进行softmax回归，和交叉熵损失计算，然后求平均值
    with tf.variable_scope('soft_loss'):
        # 求平均交叉熵损失, 返回列表
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict))

    # 4.BP梯度下降优化损失
    with tf.variable_scope('optimizer'):
        train_op = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

    # 5.准确率计算
    with tf.variable_scope('acc'):
        equal_list = tf.equal(tf.argmax(y_true, axis=1), tf.argmax(y_predict, axis=1))
        # equal_lsit None个样本，[1,0,1,0,0,0,0,0,..........]
        accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))

    # 收集变量
    tf.summary.scalar('losses', loss)
    tf.summary.scalar('acc', accuracy)
    tf.summary.histogram('weights', weight)
    tf.summary.histogram('biases', bias)

    # 变量初始化op
    init_op = tf.global_variables_initializer()

    # 定义合并变量的op
    merged = tf.summary.merge_all()

    # 创建saver,保存模型
    saver = tf.train.Saver()

    # 6.开启会话，进行训练
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 建立events文件，然后写入
        filewriter = tf.summary.FileWriter('./tmp/summary/test/', graph=sess.graph)

        if FLAGS.is_train == 1:
            # 迭代训练，更新参数进行预测
            for i in range(2000):
                # 取出真实的目标值和特征值
                mnist_x, mnist_y = mnist.train.next_batch(100)

                # 运行train_op训练
                sess.run(train_op, feed_dict={x: mnist_x, y_true: mnist_y})

                # 写入每步训练的值
                summary = sess.run(merged, feed_dict={x: mnist_x, y_true: mnist_y})
                filewriter.add_summary(summary, i)

                # 输出准确率
                print('训练第%d步，准确率为：%f' % (i, sess.run(accuracy, feed_dict={x: mnist_x, y_true: mnist_y})))

            # 保存模型
            saver.save(sess, './tmp/ckpt/fc_model')
        else:
            # 加载模型
            saver.restore(sess, './tmp/ckpt/fc_model')

            # 如果是0，进行预测
            for i in range(100):
                # 每次测试一张图片
                x_test, y_test = mnist.test.next_batch(1)
                print('第%d张图片，手写数字是%d,预测结果是%d' % (
                    i,
                    tf.argmax(y_test, axis=1).eval(),
                    tf.argmax(sess.run(y_predict, feed_dict={x: x_test, y_true: y_test}), 1).eval()
                ))

    return None


# 定义一个初始化权重的函数
def weight_variables(shape):
    w = tf.Variable(tf.random_normal(shape=shape, mean=0.1, stddev=1.0))
    return w


# 定义一个初始化偏置的函数
def bias_variables(shape):
    b = tf.Variable(tf.constant(0.0, shape=shape))
    return b


def model():
    """
    自定义的卷机模型
    :return:
    """
    # 1.准备数据占位符
    with tf.variable_scope('data'):
        x = tf.placeholder(tf.float32, [None, 784])
        y_true = tf.placeholder(tf.int32, [None, 10])

    # 2.卷积层1: 卷积：5*5*1,32个，strides=1、激活、池化
    with tf.variable_scope('conv1'):
        # 初始化权重
        w_conv1 = weight_variables([5, 5, 1, 32])
        b_conv1 = bias_variables([32])

        # 对x进行形状的改变, 不知道形状时填-1，不能填None
        x_reshape = tf.reshape(x, [-1, 28, 28, 1])

        # [None,28,28,1] -----> [None,28,28,32]
        x_relu1 = tf.nn.relu(tf.nn.conv2d(x_reshape, w_conv1, strides=[1, 1, 1, 1], padding='SAME') + b_conv1)

        # 池化 2*2， strides=2
        x_pool1 = tf.nn.max_pool(x_relu1, [1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # 3.卷积层2  卷积：5*5*32,64个filter，strides=1、激活、池化
    with tf.variable_scope('conv2'):
        # 初始化权重
        w_conv2 = weight_variables([5, 5, 32, 64])
        b_conv2 = bias_variables([64])

        # [None,28,28,1] -----> [None,28,28,32]
        x_relu2 = tf.nn.relu(tf.nn.conv2d(x_pool1, w_conv2, strides=[1, 1, 1, 1], padding='SAME') + b_conv2)

        # 池化 2*2， strides=2
        x_pool2 = tf.nn.max_pool(x_relu2, [1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # 4.全连接层 [None, 7,7,64] --> [None,7*7*64] *[7*7*64，10] +[10] = [None,10]
    with tf.variable_scope('conv2'):
        # 初始化权重
        w_fc = weight_variables([7 * 7 * 64, 10])
        b_fc = bias_variables([10])

        # 修改x形状
        x_fc_reshape = tf.reshape(x_pool2, [-1, 7 * 7 * 64])

        # 进行矩阵运算，得出每个样本的10个结果
        y_predict = tf.matmul(x_fc_reshape, w_fc) + b_fc

    return x, y_true, y_predict


def cnnv_fc():
    # 获取真实数据
    mnist = input_data.read_data_sets('./data/mnist/', one_hot=True)

    # 定义模型，得出输出
    x, y_true, y_predict = model()

    # 进行交叉熵损失计算
    # 3.进行softmax回归，和交叉熵损失计算，然后求平均值
    with tf.variable_scope('soft_loss'):
        # 求平均交叉熵损失, 返回列表
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict))

    # 4.BP梯度下降优化损失
    with tf.variable_scope('optimizer'):
        train_op = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss)

    # 5.准确率计算
    with tf.variable_scope('acc'):
        equal_list = tf.equal(tf.argmax(y_true, axis=1), tf.argmax(y_predict, axis=1))
        # equal_lsit None个样本，[1,0,1,0,0,0,0,0,..........]
        accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))

    # 变量初始化op
    init_op = tf.global_variables_initializer()

    # 6.开启会话，进行训练
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 迭代训练，更新参数进行预测
        for i in range(2000):
            # 取出真实的目标值和特征值
            mnist_x, mnist_y = mnist.train.next_batch(100)

            # 运行train_op训练
            sess.run(train_op, feed_dict={x: mnist_x, y_true: mnist_y})

            # 输出准确率
            print('训练第%d步，准确率为：%f' % (i, sess.run(accuracy, feed_dict={x: mnist_x, y_true: mnist_y})))




if __name__ == '__main__':
    # full_connectes()
    cnnv_fc()

