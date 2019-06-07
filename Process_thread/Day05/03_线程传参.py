# @Project:AID1810
# @Author:biabu
# @Date:18-12-25 上午10:10
# @File_name:03_线程传参.py
# @IDE:PyCharm


from threading import Thread
import time


# 线程函数
def f1(name, seconds):
    print("%s 线程开始执行" % name)
    time.sleep(seconds)
    print("%s 线程执行完毕，时间为%d秒" % (name,seconds))


if __name__ == '__main__':
    # 创建线程列表，存放线程对象
    threads = []
    for i in range(3):
        t = Thread(target=f1,args=(i+1,2))
        threads.append(t)
        t.start()
        t.join()
    # 回收线程
    # for m in threads:
    #     m.join()