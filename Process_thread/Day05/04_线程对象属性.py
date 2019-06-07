# @Project:AID1810
# @Author:biabu
# @Date:18-12-25 上午10:51
# @File_name:04_线程对象属性.py
# @IDE:PyCharm


from threading import Thread, currentThread
import time


def f1():
    print("线程对象ｔ属性测试")
    time.sleep(1)
    print("%s 子线程执行完毕" % currentThread().getName())


if __name__ == '__main__':
    t = Thread(target=f1)
    # 设置守护线程，必须放在start之前,不能和join连用
    t.setDaemon(True)
    t.daemon = True
    t.start()
    # 线程中可利用name属性或者getName()方法获取线程名
    print("线程名称", t.name)
    print("线程名称", t.getName())
    t.setName("Tedu-1")
    print("线程名称", t.name)
    t.join()
