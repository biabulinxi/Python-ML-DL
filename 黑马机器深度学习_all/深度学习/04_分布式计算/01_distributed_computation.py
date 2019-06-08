# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/3 14:48
# @File_name:01_distributed_computation.py
# @IDE:PyCharm

import tensorflow as tf


FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('job_name','','启动服务的类型')
tf.app.flags.DEFINE_string('task_index', 0 ,'启动哪台服务')


def main(argv):
    # 定义全局计数钩子
    global_step = tf.contrib.framework.get_or_create_globel_step()

    # 指定集群描述对象
    cluster = tf.train.ClusterSpec({'ps':['176.234.9.17:2223'],'worker':["176.234.9.59:2222"]})

    # 创建不同的服务，ps, worker
    server = tf.train.Server(cluster,job_name=FLAGS.job_name,task_index=FLAGS.task_index)

    # 根据不同的服务做不同的事情，ps：参数计算，worker:模型计算训练
    if FLAGS.job_name == 'ps':
        # 参数服务器什么也不用干，只需等待传递参数
        server.join()
    else:
        worker_device = '/job:worker/task:0/gpu:0/'

        # 指定哪个设备运行
        with tf.device(tf.train.replica_device_setter(
            worker_device=worker_device,
            cluster=cluster
        )):
            # 简单进行矩阵乘法运算
            a = tf.Variable([[1,2,3,4]])
            b = tf.Variable([[1],[2],[3][4]])
            mat = tf.matmul(a,b)

        # 创建分布式会话
        with tf.train.MonitoredTrainingSession(
            master='grpc://176.234.9.59',  # 指定主work
            is_chief=(FLAGS.task_index == 0),  # 判断是否为主worker
            config=tf.ConfigProto(log_device_placement=True),  # 打印设备信息
            hooks=[tf.train.StopAtStepHook(last_step=200)]
        ) as mon_sess:
            while not mon_sess.should_stop():
                mon_sess.run(mat)


if __name__ == '__main__':
    tf.app.run()

