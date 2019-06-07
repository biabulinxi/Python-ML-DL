# @Project:AID1810
# @Author:biabu
# @Date:18-12-20 下午5:35
# @File_name:06_multiProcessing.py
# @IDE:PyCharm

import time
from multiprocessing import Process


# 事件１
def fun1():
    print("子进程在做事件１")


# 创建一个进程
p = Process(target=fun1)
# 进程启动,执行fun1函数中的代码
p.start()

time.sleep(0.1)
# 父进程
print("父进程在做事")
