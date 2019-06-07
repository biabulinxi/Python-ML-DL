# @Project:AID1810
# @Author:biabu
# @Date:18-12-20 下午2:31
# @File_name:02_僵尸进程.py
# @IDE:PyCharm

import os
import time

pid = os.fork()

if pid < 0:
    print("创建进程失败")
elif pid == 0:
    print("子进程:%d" % os.getpid())
else:
    print("父进程:%d" % os.getpid())
    time.sleep(50)