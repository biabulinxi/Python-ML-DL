# @Project:AID1810
# @Author:biabu
# @Date:18-12-25 上午11:18
# @File_name:05_自定义线程类.py
# @IDE:PyCharm

from threading import Thread
import time


class MyThread(Thread):
    def __init__(self,number):
        self.number = number
        super().__init__()

    def f1(self):
        print("自定义线程类启动，倒计时开启")
        for i in range(self.number,0,-1):
            print(i)
            time.sleep(1)
        print("自定义线程类结束")

    def run(self):
        self.f1()


if __name__ == '__main__':
    t = MyThread(5)
    t.start()
    t.join()
    print("主线程结束")



