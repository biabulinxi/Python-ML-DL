# @Project:AID1810
# @Author:biabu
# @Date:18-12-25 下午3:51
# @File_name:09_多线程多进程效率测试.py
# @IDE:PyCharm


# CPU密集型
def CPU(x, y):
    z = 0
    while z < 7000000:
        x += 1
        y += 1
        z += 1


# I/O密集型
def write():
    with open('test.txt', 'a') as f:
        for i in range(1500000):
            f.write('Hello world')


def read():
    with open('test.txt', 'r') as f:
        f.readline()


def IO():
    write()
    read()


# ******************************************* #
from multiprocessing import Process
from threading import Thread
import time

'''
# 多线程处理ＣＰＵ密集型:10.31秒
begin1 = time.time()
threads = []
for i in range(10):
    t = Thread(target=CPU,args=(1,1))
    threads.append(t)
    t.start()

for m in threads:
    m.join()

end1 = time.time()
print("多线程处理CPU密集型时间：%.2f" % (end1 - begin1))
'''

'''
# 多进程处理ＣＰＵ密集型:4.95秒
begin2 = time.time()
process = []
for i in range(10):
    p = Process(target=CPU,args=(1,1))
    process.append(p)
    p.start()

for m in process:
    m.join()

end2 = time.time()
print("多进程处理CPU密集型时间：%.2f" % (end2 - begin2))
'''


# 多线程处理I/O密集型:0.80秒
begin1 = time.time()
threads = []
for i in range(10):
    t = Thread(target=IO)
    threads.append(t)
    t.start()

for m in threads:
    m.join()

end1 = time.time()
print("多线程处理IO密集型时间：%.2f" % (end1 - begin1))


# 多进程处理I/O密集型:0.34秒
# begin2 = time.time()
# process = []
# for i in range(10):
#     p = Process(target=IO)
#     process.append(p)
#     p.start()
#
# for m in process:
#     m.join()
#
# end2 = time.time()
# print("多进程处理CPU密集型时间：%.2f" % (end2 - begin2))
#




