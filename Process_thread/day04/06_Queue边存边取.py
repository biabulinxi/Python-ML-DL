# @Project:AID1810
# @Author:biabu
# @Date:18-12-24 下午2:31
# @File_name:06_Queue边存边取.py
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
    while True:
        try:
            # 设置阻塞超时，超过１秒不阻塞
            print(q.get(timeout=1))
        except Exception:
            print("此队列已空")
            break


if __name__ == '__main__':
    # 创建队列
    q = Queue(4)
    p1 = Process(target=write)
    p2 = Process(target=read)
    # 边存边取，同时启动进程，同时关闭
    p1.start()
    p2.start()
    p1.join()
    p2.join()



