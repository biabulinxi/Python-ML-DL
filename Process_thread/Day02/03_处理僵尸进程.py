# @Project:AID1810
# @Author:biabu
# @Date:18-12-20 下午2:47
# @File_name:03_处理僵尸进程.py
# @IDE:PyCharm


import os
import time
import sys

pid = os.fork()

if pid < 0:
    print("失败")
elif pid == 0:
    print("我是子进程，我３秒后就要死了")
    time.sleep(3)
    sys.exit("子进程退出了") #
else:
    # wait()为阻塞函数,子进程退出后会解除阻塞
    pid, status = os.wait()
    print("pid",pid)
    print("status",status)
    print("我是父进程，我的儿子死了，我已经办完丧事了")

    while True:
        pass
