# @Project:AID1810
# @Author:biabu
# @Date:18-12-24 下午2:42
# @File_name:07_进程池Queue.py
# @IDE:PyCharm

from multiprocessing import Pool, Manager


# 子进程１负责放
def write():
    for s in ["A", "B", "C"]:
        q.put(s)


# 子进程2负责取
def read():
    while True:
        try:
            print(q.get(block=False))
        except:
            break


if __name__ == '__main__':
    # 创建进程池管道
    q = Manager().Queue()
    pool = Pool()
    # 添加任务,用apply阻塞，先放再去
    pool.apply(func=write)
    pool.apply(func=read)
    # 关闭进程池
    pool.close()
    pool.join()
