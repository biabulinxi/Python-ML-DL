# @Project:AID1810
# @Author:biabu
# @Date:18-12-24 下午2:57
# @File_name:08_进程池返回平方.py
# @IDE:PyCharm


from multiprocessing import Pool, Manager


# 子进程１放
def f1(n):
    for i in range(1, n + 1):
        # 放元祖到队列
        q.put((2, i))


# 子进程２取
def f2(n):
    for i in range(n):
        m, n = q.get()
        # 2的n次方
        print(m ** n)


if __name__ == '__main__':
    # 创建消息队列
    q = Manager().Queue()
    pool = Pool()
    pool.apply_async(func=f1, args=(10,))
    pool.apply_async(func=f2, args=(10,))
    pool.close()
    pool.join()
