# @Project:AID1810
# @Author:biabu
# @Date:18-12-25 下午2:46
# @File_name:08_Thread_Event.py
# @IDE:PyCharm


from threading import Thread, Event
import time


# 定义全局变量
s = None


# 分支线程事件函数
def python():
    global s
    s = "我待Python如初恋"
    # 设置e为Ture,则wait不阻塞
    # e.set()


if __name__ == '__main__':
    # 创建事件对象
    e = Event()
    t = Thread(target=python)
    t.start()
    print("主线程:Python虐我千百遍")
    # 初始设置e为False状态,则wait被阻塞
    e.wait()
    if s == "我待Python如初恋":
        print("恭喜，薪资过万")
    else:
        print("下个班在等你")






