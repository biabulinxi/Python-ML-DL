# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/3 11:25
# @File_name:captcha-train.py
# @IDE:PyCharm

import tensorflow as tf


FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('captcha_dir','./tfrecords/captcha.tfrecords','验证码数据的路径')
tf.app.flags.DEFINE_integer('batch_size',100,'每批次读取的数量')
tf.app.flags.DEFINE_integer('letter_num',26,'每个目标值取的字母的可能性个数')
tf.app.flags.DEFINE_integer('label_num',4,'每个样本的目标值数量')


def read_and_decode():
    """
    读取数据API
    :return:image_batch,label_batch
    """
    # 1.构建文件队列
    file_queue = tf.train.string_input_producer([FLAGS.captcha_dir])

    # 2.构建阅读器，读取文件内容，默认一个样本
    reader = tf.TFRecordReader()

    # 3.读取内容
    key, value = reader.read(file_queue)

    # 4.解析tfrecords的example
    features = tf.parse_single_example(value,features={
        'image':tf.FixedLenFeature([],tf.string),
        'label':tf.FixedLenFeature([],tf.string),
    })
    # 进行解码
    image = tf.decode_raw(features['image'],tf.uint8)
    label = tf.decode_raw(features['label'],tf.uint8)

    # 5.改变形状
    image_reshape = tf.reshape(image,[20,80,3])
    label_reshape = tf.reshape(label,[4])

    # 6.进行批处理
    image_batch, label_batch = tf.train.batch([image_reshape,label_reshape],batch_size=FLAGS.batch_size,num_threads=10,capacity=FLAGS.batch_size)

    return image_batch, label_batch


# 定义一个初始化权重的函数
def weight_variables(shape):
    w = tf.Variable(tf.random_normal(shape=shape, mean=0.1, stddev=1.0))
    return w


# 定义一个初始化偏置的函数
def bias_variables(shape):
    b = tf.Variable(tf.constant(0.0, shape=shape))
    return b


def fc_model(image):
    """
    进行预测
    :param image: 图片特征值
    :return: y_predict 预测值
    """
    with tf.variable_scope('model'):
        # 将图片数据转换成二维数据
        image_reshape = tf.reshape(image,[-1,20*80*3])

        # 随机初始化权重和偏置
        weights = weight_variables([20*80*3, 4*26])
        bias = bias_variables([4*26])

        # 进行全连接层计算
        y_predict = tf.matmul(tf.cast(image_reshape,tf.float32),weights) + bias

    return y_predict


def predict_to_onehot(label):
    """
    将文件的目标值转换成one-hot编码
    :param label: 目标值
    :return: label_onehot
    """
    # 进行one_hot编码转换，提供给交叉熵损失进行计算，准确率计算[100,4,26]
    label_onehot = tf.one_hot(label,depth=FLAGS.letter_num,axis=2,on_value=1.0)
    return label_onehot




def captcharec():
    """
    验证码识别程序
    :return:None
    """
    # 1.读取验证码的数据文件
    image_batch, label_batch = read_and_decode()

    # 2.通过输入图片特征数据，建立模型，得出预测结果，使用一层全连接层神经网络
    # matrix [100, 20 * 80 * 3] * [20 * 80 * 3, 4*26] + [104] = [100,4*26]
    y_predict = fc_model(image_batch)
    print(y_predict)

    # 3.先把目标值转换成one-hot编码，[100,4,26]
    y_true = predict_to_onehot(label_batch)

    # 4.交叉熵损失计算，进行softmax回归，和交叉熵损失计算，然后求平均值
    with tf.variable_scope('soft_loss'):
        # 求平均交叉熵损失, 返回列表
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(y_true,[FLAGS.batch_size, FLAGS.label_num * FLAGS.letter_num]), logits=y_predict))

    # 5.BP梯度下降优化损失
    with tf.variable_scope('optimizer'):
        train_op = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

    # 6.准确率计算, 每批次数据样本的预测准确率，三维比较
    with tf.variable_scope('acc'):
        # equal_lsit None个样本，[1,0,1,0,0,0,0,0,..........]
        equal_list = tf.equal(tf.argmax(y_true, axis=2), tf.argmax(tf.reshape(y_predict,[100,4,26]), axis=2))
        accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))

    # 变量初始化op
    init_op = tf.global_variables_initializer()

    # 7.开启会话，进行训练
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 定义线程协调器和开启线程，
        coord = tf.train.Coordinator()

        # 开启线程取运行读取文件程序
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 训练识别程序
        # 迭代训练，更新参数进行预测
        for i in range(5000):
            # 运行train_op训练
            sess.run(train_op)
            # 输出准确率
            print('训练第%d步，准确率为：%f' % (i, sess.run(accuracy)))

        # 回收线程
        coord.request_stop()
        coord.join(threads)

    return None


if __name__ == '__main__':
    captcharec()



