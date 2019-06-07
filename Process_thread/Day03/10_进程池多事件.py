# @Project:AID1810
# @Author:biabu
# @Date:18-12-21 下午5:13
# @File_name:10_进程池多事件.py
# @IDE:PyCharm


from multiprocessing import Pool
import time


# 事件1
def fun1():
    print("我是事件1")


# 事件2
def fun2():
    print("我是事件2")


# 事件3
def fun3():
    print("我是事件3")


# 创建进程池
pool = Pool(processes=1)

# 添加任务
for i in [fun1, fun2, fun3]:
    # pool.apply_async(func=i)
    pool.apply(func=i)

# 关闭进程池
pool.close()

# 回收进程池
pool.join()
