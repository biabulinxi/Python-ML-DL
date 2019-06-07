# @Project:AID1810
# @Author:biabu
# @Date:18-12-21 下午3:11
# @File_name:08_自定义进程类练习.py
# @IDE:PyCharm

from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self,n):
        self.n = n
        super().__init__()

    def countdown(self):
        print('%d秒倒计时开始:' % self.n)
        for i in range(self.n,0,-1):
            print(i)
            time.sleep(1)
        print('结束')

    def run(self):
        self.countdown()


if __name__ == '__main__':
    start = time.time()
    p = MyProcess(5)
    # super(MyProcess,p).__init__()
    p.start()
    p.join()
    end = time.time()
    print("执行时间%.2f" % (end - start))