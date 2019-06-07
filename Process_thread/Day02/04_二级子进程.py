# @Project:AID1810
# @Author:biabu
# @Date:18-12-20 下午3:45
# @File_name:04_二级子进程.py
# @IDE:PyCharm

import os

# 事件１
def fun1():
    print("事件1")

# 事件2
def fun2():
    print("事件2")

pid = os.fork()
if pid < 0:
    print("一级子进程创建失败")
elif pid == 0:
    p = os.fork()
    if p < 0:
        print("二级子进程创建失败")
    elif p == 0:
        fun2()
    else:
        os._exit(0)  # 一级子进程结束
else:
    pid, status = os.wait()   # 阻塞，处理一级子进程
    fun1()  # 父进程做事件１
