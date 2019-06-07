# @Project:AID1810
# @Author:biabu
# @Date:18-12-25 上午9:51
# @File_name:01_Tread示例.py
# @IDE:PyCharm

from threading import Thread
import os
import time


# 线程函数
def music():
    for i in range(2):
        time.sleep(2)
        print("分支线程%s播放怒放的生命,我的主线程是%s" %
              (os.getpid(),os.getppid()))

if __name__ == '__main__':
    # 创建线程对象
    t = Thread(target=music)
    t.start()
    for i in range(2):
        time.sleep(3)
        print("主线程%s播放学猫叫" % os.getpid())
    t.join()

##################################
# 主线程和分支线程的pid是一样的，说明主线程和分支线程线程都属于同于进程
