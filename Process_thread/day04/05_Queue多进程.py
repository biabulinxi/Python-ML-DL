# @Project:AID1810
# @Author:biabu
# @Date:18-12-24 下午2:11
# @File_name:05_Queue多进程.py
# @IDE:PyCharm


from multiprocessing import Queue, Process


# 子进程１在队列中添加消息
def write():
    for i in range(10):
        if q.full():
            print('此队列已满')
            break
        q.put(i)


# 子进程2在队列中添加消息
def read():
    if not q.empty():
        while True:
            try:
                # 设置不阻塞
                print(q.get(block=False))
            except Exception:
                print("此队列已空")
                break


if __name__ == '__main__':
    # 创建队列
    q = Queue(4)
    p1 = Process(target=write)
    p2 = Process(target=read)
    # 让p1进程先放完所有数据
    p1.start()
    p1.join()
    # 再执行p2,获取数据
    p2.start()
    p2.join()



