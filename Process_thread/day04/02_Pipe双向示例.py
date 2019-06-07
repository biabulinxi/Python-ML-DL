# @Project:AID1810
# @Author:biabu
# @Date:18-12-24 上午11:02
# @File_name:02_Pipe双向示例.py
# @IDE:PyCharm


from multiprocessing import Pipe
from multiprocessing import Process


# 子进程会复制父进程的接收和发送端，要收发信息
# 需一个进程只留一个端口

# 定义事件函数
def recive():
    # 关闭子进程的发送端
    conn1.close()
    while True:
        try:
            data = conn2.recv()
            print("子进程接收数据:", data)
        except EOFError:
            break


# 父进程代码
# 创建管道（双向）
conn1, conn2 = Pipe()
# 创建进程对象
p = Process(target=recive)
p.start()

# 关闭父进程的接收端
conn2.close()
# 父进程向管道发送数据
for content in ["聂风", "步惊云", "孔慈"]:
    conn1.send(content)
# 关闭父进程的发送
conn1.close()
p.join()


# conn1 发送
# conn2 接收
# 1. 父进程：conn2关闭，conn1发送
# 2. 子进程：conn1关闭，conn2发送
