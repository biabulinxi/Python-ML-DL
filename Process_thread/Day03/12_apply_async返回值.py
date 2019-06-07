# @Project:AID1810
# @Author:biabu
# @Date:18-12-21 下午5:44
# @File_name:12_apply_async返回值.py
# @IDE:PyCharm


from multiprocessing import Pool
import time


def f1(n):
    # time.sleep(1)
    return n**2


if __name__ == '__main__':
    begin = time.time()
    # 创建进程池对象
    pool = Pool(processes=1)
    # 存放apply_async()返回值
    rlist = []
    for i in range(1,7):
        robj = pool.apply_async(f1,args=(i,))
        rlist.append(robj)
    # 遍历出rlist中的每个对象，获取函数返回值
    for i in rlist:
        print(i.get())

    pool.close()
    pool.join()