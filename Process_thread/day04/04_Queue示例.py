# @Project:AID1810
# @Author:biabu
# @Date:18-12-24 上午11:37
# @File_name:04_Queue示例.py
# @IDE:PyCharm

import time
from multiprocessing import Queue
from multiprocessing import Process

# 创建消息队列
q = Queue(maxsize=3)

'''
# put()值
q.put("消息1")
q.put("消息2")
q.put("消息3")



time.sleep(0.1)

# get()值
while True:
    if q.empty():
        print('队列为空')
        break
    print(q.get())
'''

# full()
i = 0
while True:
    if q.full():
        print('队列已满')
        break
    q.put('消息：%d' % i)
    i += 1

print("当前队列中有%d条消息" % i)
print("当前队列中有%d条消息" % q.qsize())
