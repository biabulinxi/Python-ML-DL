# @Project:AID1810
# @Author:biabu
# @Date:18-12-21 上午10:59
# @File_name:04_多进程.py
# @IDE:PyCharm

from multiprocessing import Process
import os
import time


start = time.time()


# 事件1
def sing():
    print("唱歌进程启动，我的父进程是:%d" % os.getppid())
    time.sleep(1)


# 事件2
def dance():
    print("跳舞进程启动，我的父进程是:%d" % os.getppid())
    time.sleep(1)


# 事件3
def eat():
    print("吃货进程启动，我的父进程是:%d" % os.getppid())
    time.sleep(1)


# 创建进程对象
# 定义空列表，存放进程
processes = []
for i in [sing, dance, eat]:
    p = Process(target=i)
    # 把进程放入列表,等待join回收
    processes.append(p)
    # 启动进程
    p.start()
    # p.join()不能写在此处，会阻塞成为顺序执行

# 回收进程
for process in processes:
    process.join()


# 创建进程对象
# p1 = Process(target=sing)
# p2 = Process(target=dance())
# p3 = Process(target=eat())

# # 启动进程
# p1.start()
# p2.start()
# p3.start()
#
# # 回收进程
# p1.join()
# p2.join()
# p3.join()


end = time.time()
print("运行时间:%f" % (end - start))
