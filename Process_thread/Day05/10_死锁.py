# @Project:AID1810
# @Author:biabu
# @Date:18-12-25 下午4:36
# @File_name:10_死锁.py
# @IDE:PyCharm

from threading import Thread,Lock
import time


# 创建２个锁对象
lock1 = Lock()
lock2 = Lock()

# 线程函数１
def f1():
    # lock1加锁
    lock1.acquire()
    print("线程1 锁住了lock1")
    time.sleep(0.1)

    # lock2加锁
    lock2.acquire()
    print("线程1 锁住了lock2")
    print("线程1 你好")

    # 解锁
    lock2.release()
    lock1.release()


# 线程函数２
def f2():
    # lock2加锁
    lock2.acquire()
    print("线程2 锁住了lock2")
    time.sleep(0.1)

    # lock1加锁
    lock1.acquire()
    print("线程2 锁住了lock1")
    print("线程2 你好")

    # 解锁
    lock1.release()
    lock2.release()


t1 = Thread(target=f1)
t2 = Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()