# @Project:AID1810
# @Author:biabu
# @Date:18-12-21 上午10:19
# @File_name:03_父子进程同步.py
# @IDE:PyCharm

from multiprocessing import Process

# 定义变量
name = "赵敏"


# 定义函数
def f1():
    global name
    print("子进程name=%s" % name)
    name = "周知若"
    print("子进程修改了name=%s" % name)


# 创建进程对象
p = Process(target=f1)
# 启动进程
p.start()
# 把父进程代码放start()与join()之间，完成父子进程同步做事

# 父进程
print("父进程name=%s" % name)

# 回收子进程，阻塞函数
p.join()


