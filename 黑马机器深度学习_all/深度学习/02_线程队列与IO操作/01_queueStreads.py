# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/1 14:57
# @File_name:01_queueStreads.py
# @IDE:PyCharm

import tensorflow as tf
import os


def mysync():
    """
    模拟同步先处理数据，然后在进行取数据训练
    """

    # 1. 首先定义队列,存入数据,tensor默认列表为张量，[[0.1,0.2,0.3],]
    Q = tf.FIFOQueue(3, tf.float32)
    enq_many = Q.enqueue_many([[0.1, 0.2, 0.3], ])

    # 2. 定义读取数据的过程，取数据+1，在入队列
    out_q = Q.dequeue()
    data = out_q + 1
    en_q = Q.enqueue(data)

    # 4. 开启会话
    with tf.Session() as sess:
        # 初始化队列
        sess.run(enq_many)

        # 处理数据，tensorflow当中，运行数据操作有依赖性
        for i in range(99):
            sess.run(en_q)

        # 训练数据
        for i in range(Q.size().eval()):
            print(sess.run(Q.dequeue()))


def myasync():
    """
    模拟异步存入样本，读取样本
    :return:
    """

    # 1.定义一个队列，1000
    Q = tf.FIFOQueue(1000, tf.float32)

    # 2.定义子线程要做的事  循环+1，房入队列
    var = tf.Variable(0.0)
    # 实现一个自增，tf.assign_add
    data = tf.assign_add(var, tf.constant(1.0))
    en_q = Q.enqueue(data)

    # 3.定义队列管理器op,指定多少个子线程要做什么事
    qr = tf.train.QueueRunner(Q, enqueue_ops=[en_q] * 2)

    # 初始化变量的op
    init_op = tf.global_variables_initializer()

    # 开启会话
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 开启线程协调管理器
        coord = tf.train.Coordinator()

        # 真正开启子线程, 确定主线程
        threads = qr.create_threads(sess, coord=coord, start=True)

        # 主线程，不断读取数据训练
        for i in range(300):
            print(sess.run(Q.dequeue()))

        # 回收子线程
        coord.request_stop()
        coord.join(threads)


def csvread(filelist):
    """
    读取CSV文件
    :param filelist: 文件路径+名字列表
    :return:读取的内容
    """

    # 1.构造文件队列
    file_queue = tf.train.string_input_producer(filelist)
    # 2.构造阅读器，读取队列，默认一行
    reader = tf.TextLineReader()
    key, value = reader.read(file_queue)
    # 3.对每行内容解码
    # record_defaults: 指定每一个样本的每一列的类型，指定默认值
    records = [["None"], [4]]
    example, label = tf.decode_csv(value, record_defaults=records)  # 返回每一列的值
    # 4.数据批处理,批处理大小只决定这个批次读取多少数据，不管是否重复
    example_batch, label_batch = tf.train.batch([example, label], batch_size=8, num_threads=2, capacity=9)

    # 开启会话运行结果
    with tf.Session() as sess:
        # 定义一个线程协调器
        coord = tf.train.Coordinator()

        # 开启读文件的线程
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 打印读取的内容
        print(sess.run([example_batch, label_batch]))

        # 回收子线程
        coord.request_stop()
        coord.join(threads)

    return None


def picread(filelist):
    """
    读取图片并转换成张量
    :param filelist: 文件路径+名字的列表
    :return:图片的内容张量
    """
    # 1.构造文件队列
    file_queue = tf.train.string_input_producer(filelist)

    # 2.构造阅读器读取图片内容（默认读取一张图片）
    reader = tf.WholeFileReader()
    key, value = reader.read(file_queue)
    print(value)

    # 3.对读取的图片数据进行解码
    image = tf.image.decode_jpeg(value)
    print(image)

    # 4.处理图片的大小（统一大小）
    image_resize = tf.image.resize_images(image, [200, 200])
    print(image_resize)

    # 5.图片批处理,必须固定形状维度,否则无法进行批处理
    image_resize.set_shape([200, 200, 3])
    image_batch = tf.train.batch([image_resize], batch_size=10, num_threads=2, capacity=10)
    print(image_batch)

    # 开启会话
    with tf.Session() as sess:
        # 开启线程协调管理器
        coord = tf.train.Coordinator()

        # 真正开启子线程, 确定主线程
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 主线程，不断读取数据训练
        print(sess.run(image_batch))

        # 回收子线程
        coord.request_stop()
        coord.join(threads)

    return None


# 定义cifar的数据读取命令行参数
FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('cifar_dir', './data/cifar-10-batches-bin', '文件的目录')
tf.app.flags.DEFINE_string('cifar_tfrecords', './tmp/cifar.tfrecords', '存进tfrecords文件的目录')


class CifarRead(object):
    """完成读取二进制文件，写进tfrecords,读取tfrecords
    """

    def __init__(self, filelist):
        # 文件列表
        self.file_list = filelist

        # 定义读取的二进制文件的一些属性
        self.height = 32
        self.width = 32
        self.channel = 3
        # 二进制文件每张图片的字节
        self.label_bytes = 1
        self.image_bytes = self.height * self.width * self.channel
        self.bytes = self.label_bytes + self.image_bytes

    def read_and_decode(self):
        # 1.构造文件队列
        file_queue = tf.train.string_input_producer(self.file_list)

        # 2.构造文件读取器，读取内容,每个样本的字节数
        reader = tf.FixedLengthRecordReader(self.bytes)
        key, value = reader.read(file_queue)

        # 3.解码内容
        label_image = tf.decode_raw(value, tf.uint8)

        # 4.分割出图片和标签数据，特征值和目标值
        label = tf.cast(tf.slice(label_image, [0], [self.label_bytes]), tf.int32)
        image = tf.slice(label_image, [self.label_bytes], [self.image_bytes])

        # 5.改变图片特征数据的形状
        image_reshape = tf.reshape(image, [self.height, self.width, self.channel])

        # 6.批处理
        image_batch, label_batch = tf.train.batch([image_reshape, label], batch_size=10, num_threads=2, capacity=10)

        return image_batch, label_batch

    def write_to_tfrecords(self, image_batch, label_batch):
        """
        将图片的特征值和目标值存入tfrecords
        :return:None
        :param image_batch:10张图片的特征值
        :param label_batch:10张图片的目标值
        """

        # 1.构造一个tfrecords文件
        writer = tf.python_io.TFRecordWriter(FLAGS.cifar_tfrecords)

        # 2.循环将所有样本写入文件。每张图片样本都要构造example协议
        for i in range(10):
            # 取出第i个图片的特征值和目标值
            image = image_batch[i].eval().tostring()
            label = label_batch[i].eval()[0]

            # 构造一个样本的example
            example = tf.train.Example(features=tf.train.Features(feature={
                'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image])),
                'label': tf.train.Feature(int64_list=tf.train.Int64List(value=[label])),
            }))

            # 序列化，写入单独的样本
            writer.write(example.SerializeToString())

        # 关闭
        writer.close()

        return None

    def read_from_tfrecords(self):
        # 1.构造文件队列
        file_queue = tf.train.string_input_producer([FLAGS.cifar_tfrecords])

        # 2.构造文件阅读器，读取内容，一个样本的序列化example
        reader = tf.TFRecordReader()
        key, value = reader.read(file_queue)

        # 3.解析example,返回字典格式
        features = tf.parse_single_example(value, features={
            'image': tf.FixedLenFeature([], tf.string),
            'label': tf.FixedLenFeature([], tf.int64),
        })

        # 4.解码内容，如果读取的内容是string类型的，需要进行解码
        image = tf.decode_raw(features['image'], tf.uint8)
        # 固定图片形状，方便批处理
        image_reshape = tf.reshape(image, [self.height, self.width, self.channel])
        label = tf.cast(features['label'], tf.int32)

        # 批处理读取数据
        image_batch, label_batch = tf.train.batch([image_reshape, label], batch_size=10, num_threads=2, capacity=10)

        return image_batch, label_batch

    def session(self):
        # 从原始数据，获取批处理文件
        image_batch, label_batch = self.read_and_decode()

        # 从tfrecords读取数据
        image_batch, label_batch = self.read_from_tfrecords()

        # 开启会话运行结果
        with tf.Session() as sess:
            # 定义一个线程协调器
            coord = tf.train.Coordinator()

            # 开启读文件的线程
            threads = tf.train.start_queue_runners(sess, coord=coord)

            # 存进tf.records文件
            print('开始存储')
            self.write_to_tfrecords(image_batch, label_batch)
            print('结束存储')

            # 打印读取的内容
            # print(sess.run([image_batch, label_batch]))

            # 回收子线程
            coord.request_stop()
            coord.join(threads)




if __name__ == '__main__':
    ####################################
    # mysync()
    # myasync()

    #####################################
    # # 找到文件，放入列表
    # file_name = os.listdir('./data/')
    # filelist = [os.path.join('./data/',file) for file in file_name]
    # csvread(filelist)

    ####################################
    # # 图片读取
    # file_name = os.listdir('./data/pic/')
    # filelist = [os.path.join('./data/pic/', file) for file in file_name]
    # picread(filelist)

    ###################################
    # 二进制文件读取
    file_name = os.listdir(FLAGS.cifar_dir)
    filelist = [os.path.join(FLAGS.cifar_dir, file) for file in file_name if file[-3:] == 'bin']
    cf = CifarRead(filelist)
    cf.session()
