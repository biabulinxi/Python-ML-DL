# @Project:AID1810
# @Author:biabu
# @Date:18-12-24 下午4:55
# @File_name:11_共享内存Array指定长度.py
# @IDE:PyCharm

from multiprocessing import Process,Array

def f1(n):
    # 子进程存放数据
    for i in range(n):
        arrayObj[i] = i + 1


if __name__ == '__main__':
    # 创建共享内存，只能存３个数据，但是没数据
    arrayObj = Array("i",3)
    p = Process(target=f1,args=(3,))
    p.start()
    p.join()

    for i in arrayObj:
        print("父进程",i)