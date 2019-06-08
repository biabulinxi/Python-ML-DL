# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/19 16:44
# @File_name:dqn.py
# @IDE:PyCharm

import tensorflow as tf
import cv2
import sys
import random
import numpy as np
from collections import deque
sys.path.append("game/")
import wrapped_flappy_bird as game

# 参数初始化
GAME = 'bird'
ACTIONS = 2  # 行为数
GAMMA = 0.99  # 观测的衰减率
OBSERVE = 10000  # 训练前观察视频的帧数
EXPLORE = 200000  # 探索的视频帧数
INITIAL_EPSILON = 0.0001  # 初始进行探索的几率
FINAL_EPSILON = 0.1  # 最终进行探索的几率
BATCH = 32  # 批处理大小
REPLAY_MEMORY = 50000  # 当前观察的帧数
FRAME_PER_ACTION = 1


def weight_variable(shape):
    # 从阶段正态分布，生成随机权重张量
    initial = tf.truncated_normal(shape, stddev=0.01)
    return tf.Variable(initial)


def bias_variable(shape):
    # 创建值为0.01的常数张量
    initial = tf.constant(0.01, shape=shape)
    return tf.Variable(initial)


def conv2d(x, w, stride):
    # 进行卷积运算
    return tf.nn.conv2d(x, w, strides=[1, stride, stride, 1], padding='SAME')


def max_pool_2x2(x):
    # 池化运算
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


def creatNetwork():
    # 权重初始化
    w_conv1 = weight_variable([8, 8, 4, 32])
    b_conv1 = bias_variable([32])

    w_conv2 = weight_variable([4, 4, 32, 64])
    b_conv2 = bias_variable([64])

    w_conv3 = weight_variable([3, 3, 64, 64])
    b_conv3 = bias_variable([64])

    w_fc1 = weight_variable([1600, 512])
    b_fc1 = weight_variable([512])

    w_fc2 = weight_variable([512, ACTIONS])
    b_fc2 = weight_variable([ACTIONS])

    # 输入层
    s = tf.placeholder('float', [None, 80, 80, 4])

    # 隐藏层
    h_conv1 = tf.nn.relu(conv2d(s, w_conv1, 4) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    h_conv2 = tf.nn.relu(conv2d(h_pool1, w_conv2, 2) + b_conv2)
    # h_pool2 = max_pool_2x2(h_conv1)

    h_conv3 = tf.nn.relu(conv2d(h_conv2, w_conv3, 1) + b_conv3)

    h_conv3_flat = tf.reshape(h_conv3, [-1, 1600])

    h_fc1 = tf.nn.relu(tf.matmul(h_conv3_flat, w_fc1) + b_fc1)

    # 输出层
    readout = tf.matmul(h_fc1, w_fc2) + b_fc2

    return s, readout, h_fc1


def trainNetwork(s, readout, h_fc1, sess):
    # 定义损失函数
    a = tf.placeholder('float', [None, ACTIONS])
    y = tf.placeholder('float', [ACTIONS])
    readout_action = tf.reduce_sum(tf.multiply(readout, a), reduction_indices=1)
    cost = tf.reduce_mean(tf.square(y - readout_action))
    train_step = tf.train.AdamOptimizer(1e-6).minimize(cost)

    # 运行游戏，与模拟器进行通信
    game_state = game.GameState()

    # 将之前的观察结果存储在回放内存中
    D = deque()

    # 输出日志文件
    a_file = open('logs_' + GAME + '/readout.txt', 'w')
    h_file = open('logs_' + GAME + '/hidden.txt', 'w')

    # 获取初始状态，进行图片处理
    do_nothing = np.zeros(ACTIONS)
    do_nothing[0] = 1
    x_t, r_0, terminal = game_state.frame_step(do_nothing)
    # OpenCV 进行图片处理，cv2.imwrite('x_t.jpg',x_t)
    x_t = cv2.cvtColor(cv2.resize(x_t, (80,80)), cv2.COLOR_BGR2GRAY)  # 重新设置大小，改变为灰度图
    ret, x_t = cv2.threshold(x_t, 1, 255, cv2.THRESH_BINARY)  # 将图片二原色化
    s_t = np.stack((x_t, x_t, x_t, x_t), axis=2)

    # 保存加载网络模型
    saver = tf.train.Saver()
    sess.run(tf.initialize_all_variables())
    checkpoint = tf.train.get_checkpoint_state('saved_networks')
    """
    if checkpoint and checkpoint.model_checkpoint_path:
        saver.restore(sess, checkpoint.model_checkpoint_path)
        print("Successfully loaded:", checkpoint.model_checkpoint_path)
    else:
        print("Could not find old network weights")
    """

    # 开始训练
    epsilon = INITIAL_EPSILON
    t = 0
    while 'flappy bird' != 'angry bird':
        # 选择一个行为，进行贪婪递增 epsilon
        readout_t = readout.eval(feed_dict = {s: [s_t]})[0]
        a_t = np.zeros([ACTIONS])
        action_index = 0
        if t % FRAME_PER_ACTION == 0:
            if random.random() <= epsilon:
                print("----------Random Action----------")
                action_index = random.randrange(ACTIONS)
                a_t[random.randrange(ACTIONS)] = 1
            else:
                action_index = np.argmax(readout_t)
                a_t[action_index] = 1
        else:
            a_t[0] = 1 # do nothing

        # 减小 epsilon
        if epsilon > FINAL_EPSILON and t > OBSERVE:
            epsilon -= (INITIAL_EPSILON - FINAL_EPSILON) / EXPLORE

        # 运行选择的状态，并观察下一个状态，同时进行奖励
        x_t1_colored, r_t, terminal = game_state.frame_step(a_t)
        x_t1 = cv2.cvtColor(cv2.resize(x_t1_colored, (80, 80)), cv2.COLOR_BGR2GRAY)
        ret, x_t1 = cv2.threshold(x_t1, 1, 255, cv2.THRESH_BINARY)
        x_t1 = np.reshape(x_t1, (80, 80, 1))
        # s_t1 = np.append(x_t1, s_t[:,:,1:], axis = 2)
        # print (s_t.shape)
        s_t1 = np.append(x_t1, s_t[:, :, :3], axis=2)

        # 将训练结果进行存储
        D.append((s_t, a_t, r_t, s_t1, terminal))
        if len(D) > REPLAY_MEMORY:
            D.popleft()

        # 观察完毕后，只进行训练
        if t > OBSERVE:
            # 最小化一个批处理样本
            minibatch = random.sample(D, BATCH)
            # 获得batch变量
            s_j_batch = [d[0] for d in minibatch]
            # print (s_j_batch.shape)
            a_batch = [d[1] for d in minibatch]
            # print (a_batch.shape)
            r_batch = [d[2] for d in minibatch]
            # print (r_batch.shape)
            s_j1_batch = [d[3] for d in minibatch]
            # print (s_j1_batch.shape)

            y_batch = []
            readout_j1_batch = readout.eval(feed_dict={s: s_j1_batch})
            for i in range(0, len(minibatch)):
                terminal = minibatch[i][4]
                # if terminal, only equals reward
                if terminal:
                    y_batch.append(r_batch[i])
                else:
                    y_batch.append(r_batch[i] + GAMMA * np.max(readout_j1_batch[i]))

            # 进行梯度
            train_step.run(feed_dict={
                y: y_batch,
                a: a_batch,
                s: s_j_batch}
            )

        # 更新参数
        s_t = s_t1
        t += 1

        # ，每迭代10000次，保存一次模型
        if t % 10000 == 0:
            saver.save(sess, 'saved_networks/' + GAME + '-dqn', global_step=t)

        # 输出信息
        state = ""
        if t <= OBSERVE:
            state = "observe"
        elif t > OBSERVE and t <= OBSERVE + EXPLORE:
            state = "explore"
        else:
            state = "train"

        print("TIMESTEP", t, "/ STATE", state, "/ EPSILON", epsilon, "/ ACTION", action_index, "/ REWARD", r_t, "/ Q_MAX %e" % np.max(readout_t))

        # 输出信息到文件
        """
        if t % 10000 <= 100:
            a_file.write(",".join([str(x) for x in readout_t]) + '\n')
            h_file.write(",".join([str(x) for x in h_fc1.eval(feed_dict={s:[s_t]})[0]]) + '\n')
            cv2.imwrite("logs_tetris/frame" + str(t) + ".png", x_t1)
        """


def playGame():
    sess = tf.InteractiveSession()
    s, readout, h_fc1 = creatNetwork()
    trainNetwork(s, readout, h_fc1, sess)


if __name__ == '__main__':
    playGame()
