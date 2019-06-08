# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/1 11:30
# @File_name:02_linearRegression.py
# @IDE:PyCharm


import tensorflow as tf
import os

# 关闭tensorflow的警告信息
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

################################################################
# 训练参数问题：trainable
# 学习率和步数设置
# 添加权重参数，损失值等在tensorflow观察的情况: 1. 收集变量，2. 合并变量写入事件文件
# 模型保存和加载

##################################################################
# 定义命令行参数：1.定义有哪些参数需要在运行时指定，2.在程序当中获取定义的命令行参数
# 第一个参数：名字，默认值，说明
tf.app.flags.DEFINE_integer('max_step',100,'模型训练的步数')
tf.app.flags.DEFINE_string('model_dir',' ','模型文件的加载路径')

# 定义获取命令行参数的名字
FALGS = tf.app.flags.FLAGS


def myregression():
    """
    自定义一个线性回归预测
    :return:None
    """
    with tf.variable_scope('data'):
        #########
        # 1.准备数据，特征值和目标值
        x = tf.random_normal([100,1],mean=1.75,stddev=0.5,name='x_data')
        # 矩阵相乘必须为二维
        y_true = tf.matmul(x,[[0.7]]) + 0.8

    with tf.variable_scope('model'):
        ##########
        # 2. 建立线性回归模型，y = kx + b
        # 随机初始化k,b，计算优化损失
        # 用变量定义才能优化, trainable: 指定变量是否被训练
        weights = tf.Variable(tf.random_normal([1,1],mean=0.0,stddev=1.0),name='w')
        bias = tf.Variable(0.0,name='b')

        y_predict = tf.matmul(x,weights)+bias

    with tf.variable_scope('loss'):
        ##################
        # 3. 建立损失函数，均方误差
        loss = tf.reduce_mean(tf.square(y_true - y_predict))

    with tf.variable_scope('optimizer'):
        ##################
        # 4. 梯度下降损失优化 leaning_rate: 0~1,2,3,5,6,7,10
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    ###########################
    # 初始化变量
    init_op = tf.global_variables_initializer()

    ##########################
    # 收集tensor
    tf.summary.scalar('losses',loss)
    tf.summary.histogram('weight',weights)
    # 合并tensor的op
    merge = tf.summary.merge_all()

    ########################
    # 模型保存
    saver = tf.train.Saver()

    # 开启会话运行程序
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 打印随机初始化的变量w,b
        print('随机初始化的参数权重为：%f, 偏置为：%f' % (weights.eval(), bias.eval()))

        # 把程序的图结构写入事件文件,graph:把指定的图写入文件当中
        filewriter = tf.summary.FileWriter('C:/Users/Pycharm/AID1810/tensorboard/tmp/summary/linear', graph=sess.graph)

        # 加载模型，覆盖模型当中随机定义的参数，从上次训练的参数结果开始、
        if os.path.exists('C:/Users/Pycharm/AID1810/tensorboard/tmp/ckpt/checkpoint'):
            saver.restore(sess,FALGS.model_dir)

        # 循环运行优化
        for i in range(FALGS.max_step):
            sess.run(train_op)
            # 打印随机初始化的变量w,b
            print('第%d步，梯度下降优化的参数权重为：%f, 偏置为：%f' % (i, weights.eval(), bias.eval()))

            # 运行合并的tensor
            summary = sess.run(merge)
            filewriter.add_summary(summary,i)

        # 模型保存和加载
        saver.save(sess,FALGS.model_dir)

    return None


if __name__ == '__main__':
    myregression()
