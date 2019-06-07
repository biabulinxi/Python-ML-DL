# @Project:AID1810
# @Author:biabu
# @Date:18-12-25 下午2:14
# @File_name:06_Lock使用.py
# @IDE:PyCharm

from threading import Lock, Thread

m = 0
n = 0

# 线程函数
def f1():
    while True:
        # 凡涉及临界资源的操作，都需加锁
        # 加锁
        lock.acquire()
        if m != n:
            print("m =", m, "n =", n)
        # 释放锁
        lock.release()




if __name__ == '__main__':
    # 创建锁对象
    lock = Lock()
    t = Thread(target=f1)
    t.start()
    # 主线程
    while True:
        with lock:
            m += 1
            n += 1

    t.join()


