# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/17 10:22
# @File_name:06_forkZombie1.py
# @IDE:PyCharm

import os
import sys
import time

pid = os.fork()
if pid < 0:
    sys.exit("连接失败")
# 一级子进程
elif pid == 0:
    pid = os.fork()
    # 二级子进程
    if pid == 0:
        print('真正的事件函数，二级子进程')
    else:
        os._exit(0)
else:
    os.wait()
    print('父进程要做的事情')
    time.sleep(30)