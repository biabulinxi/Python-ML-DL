# @Project:AID1810
# @Author:biabu
# @Date:18-12-21 上午11:38
# @File_name:05_多进程传参.py
# @IDE:PyCharm


from multiprocessing import Process
import os
import time

start = time.time()


# 事件１
def smoke(name, number):
    print("抽烟进程%d启动,%s抽了%d根烟" %
          (os.getpid(), name, number))


def drink(name):
    print("drink process %s is drinking" % name)


def hair(name):
    print("hair process %s is hairing" % name)


p1 = Process(target=smoke, args=("于谦", 5))
p2 = Process(target=drink,kwargs={'name':"魏叔叔"})
p3 = Process(target=hair, args=("超哥哥",))

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

end = time.time()
print("执行时间:%.2f" % (end - start))
