# @Project:AID1810
# @Author:biabu
# @Date:18-12-24 下午3:59
# @File_name:09_共享内存（生产者消费者）.py
# @IDE:PyCharm

from multiprocessing import Value, Process, Lock


# 生产者
def makeMoney():
    for i in range(1000):
        # 加锁
        lock.acquire()
        money.value += 1
        # 释放锁
        lock.release()


# 消费者
def useMoney():
    for i in range(1000):
        # 加锁
        lock.acquire()
        money.value -= 1
        # 释放锁
        lock.release()


if __name__ == '__main__':
    # 创建共享内存
    money = Value("i", 5000)
    # 创建锁对象
    lock = Lock()
    # 创建两个进程
    p1 = Process(target=makeMoney())
    p2 = Process(target=useMoney())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("最终余额：", money.value)

