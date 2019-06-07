# @Project:AID1810
# @Author:biabu
# @Date:18-12-20 上午10:06
# @File_name:01_os.py
# @IDE:PyCharm

import os

# print("*************************")
# name = "张三丰"
#
#
# # os.fork()创建子进程
# pid = os.fork()
#
# if pid < 0:
#     print("创建新进程失败")
#
# elif pid == 0:
# # os.getpid()获得当前进程ID
# # os.getppid()获取父进程ID
#     name = "张无忌"
#     print("我是子进程%s%s,我的父进程是%s" % (name,os.getpid(),os.getppid()))
# else:
#     print("我是父进程%s%s创建了子进程%s" % (name,os.getpid(),pid))
#
# print("============结束============")


#################################

# import sys
# import os
#
# # os._exit()进程退出，后面的语句不会执行
# print("进程%d开始执行" % os.getpid())
# os._exit(0)
# print("进程%d开始退出" % os.getpid())
#
#
# # sys.exit()进程退出，后面的语句不会执行
# print("进程%d开始执行" % os.getpid())
# sys.exit("我挂了！！！")
# print("进程%d开始退出" % os.getpid())