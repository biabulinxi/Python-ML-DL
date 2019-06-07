# @Project:AID1810
# @Author:biabu
# @Date:18-12-21 下午2:10
# @File_name:06_进程对象属性.py
# @IDE:PyCharm

from multiprocessing import Process
import time


# 写一个时间函数，每隔一秒打印一次
def timing(n):
    for i in range(n):
        print(time.time())
        time.sleep(1)


#创建进程
p = Process(target=timing,args = (5,),name = "计时器")

'''
设置为守护进程，主进程结束，子进程跟着结束
设置为守护进程后，就不需使用join()回收
'''
p.daemon = True

#启动进程，start()语句后才会真正创建进程
p.start()

print("进程名称",p.name)
print("PID号",p.pid)
print("是否存活",p.is_alive())

#回收进程
p.join()



