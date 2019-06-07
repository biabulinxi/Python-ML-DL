# @Project:AID1810
# @Author:biabu
# @Date:18-12-21 下午4:42
# @File_name:09_进程池.py
# @IDE:PyCharm


from multiprocessing import Pool
import time


# 定义事件函数
def automan(n):
    print("奥特曼进入进程池",n)
    time.sleep(1)


# 创建进程池对象
pool = Pool(processes=2)
# 添加任务
for i in range(1,7):
    # pool.apply_async(func=automan,args=(i,))
    pool.apply(func=automan,args=(i,))


# 关闭进程池
pool.close()

# 回收进程池
pool.join()
