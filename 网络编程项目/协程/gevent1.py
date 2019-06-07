# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/21 17:49
# @File_name:gevent1.py
# @IDE:PyCharm

import gevent
import time

def f1(m,n):
    print("执行函数1",m,n)
    # time.sleep()不是 gevent 类型的阻塞
    time.sleep(2)
    print("函数1执行结束")


def f2():
    print("执行函数2")
    time.sleep(3)
    print("函数2执行结束")

# 创建协程对象
g1 = gevent.spawn(f1,10,20)
g2 = gevent.spawn(f2)

# 启动并阻塞等待回收协程
gevent.joinall([g1,g2])