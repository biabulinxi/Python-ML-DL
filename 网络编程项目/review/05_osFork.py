# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/17 10:15
# @File_name:05_osFork.py
# @IDE:PyCharm

import os
import sys
import time

pid = os.fork()
if pid < 0:
    sys.exit('创建进程失败')
elif pid == 0:
    print("子进程执行的事件函数")
else:
    print("父进程执行的事件函数")
    time.sleep(30)
