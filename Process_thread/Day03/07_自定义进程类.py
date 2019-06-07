# @Project:AID1810
# @Author:biabu
# @Date:18-12-21 下午2:47
# @File_name:07_自定义进程类.py
# @IDE:PyCharm

from multiprocessing import Process
import time


# 自定义进程类
class MyProcess(Process):
    def __init__(self, n):
        self.n = n
        # 使用super重新加载父类的__init__()方法
        # super(MyProcess, self).__init__()
        super().__init__()
        # Process.__init__(self)

    # 重写run方法，父类中对此方法做了自动化处理
    # 如果换了方法名，就无法执行
    def fun1(self):
        for i in range(self.n):
            print('子进程在做事')
            time.sleep(1)

    def run(self):
        self.fun1()


if __name__ == '__main__':
    start = time.time()
    p = MyProcess(3)
    p.start()
    p.join()
    print("我是父进程")
    end = time.time()
    print("执行时间:%.2f" % (end - start))
