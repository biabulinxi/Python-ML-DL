# @Project:AID1810
# @Author:biabu
# @Date:18-12-24 下午4:41
# @File_name:10_共享内存Array.py
# @IDE:PyCharm

from multiprocessing import Process, Array

# 事件函数
def f1():
    for i in shareData:
        print("子程序打印",i)
    # 修改第一个数组元素
    shareData[0] = 10


if __name__ == '__main__':
    # 开辟共享内存，存入整数列表
    # shareData为可迭代对象
    shareData = Array("i", [1,2,3,4,5])
    p = Process(target=f1)
    p.start()
    p.join()

    # 放在join()之后，子程序改完后父进程才会打印
    for i in shareData:
        print("父进程",i)





