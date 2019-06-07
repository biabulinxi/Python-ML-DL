# @Project:AID1810
# @Author:biabu
# @Date:18-12-21 下午5:31
# @File_name:11_进程池map.py
# @IDE:PyCharm


from multiprocessing import Pool
import time


def f1(n):
    # time.sleep(1)
    return n**2

# 创建进程池对象
pool = Pool(processes=1)
# 用map方式向进程池中添加任务,返回时间函数的返回值列表
rlist = pool.map(f1, range(10))
print(rlist)

pool.close()
pool.join()