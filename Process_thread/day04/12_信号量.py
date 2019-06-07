# @Project:AID1810
# @Author:biabu
# @Date:18-12-24 下午5:44
# @File_name:12_信号量.py
# @IDE:PyCharm

import os
import time
from multiprocessing import Semaphore,Process


def f1():
    print("%d 想要执行事件" % os.getpid())
    # 获取一个信号量,信号量计数器减一　
    # 减为０时，剩余事件任务被阻塞
    sem.acquire()
    print("%d 拿到信号量开始执行" % os.getpid())
    time.sleep(1)
    # 释放一个信号量，信号量计数器加一
    # 每当信号量加一，被阻塞的任务事件则释放
    sem.release()

if __name__ == '__main__':
    # 创建信号量
    sem = Semaphore(3)
    # 定义空列表，存放所有进程对象
    pList = []
    for i in range(10):
        p = Process(target = f1)
        pList.append(p)
        p.start()

    for p in pList:
        p.join()