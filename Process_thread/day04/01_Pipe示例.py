# @Project:AID1810
# @Author:biabu
# @Date:18-12-24 上午10:05
# @File_name:01_Pipe示例.py
# @IDE:PyCharm

from multiprocessing import Pipe
from multiprocessing import Process


# 子进程会复制父进程的接收和发送端，要收发信息
# 需一个进程只留一个端口

# 定义事件函数
def recive():
    # 关闭子进程的发送端
    conn2.close()
    while True:
        try:
            data = conn1.recv()
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
conn1.close()
# 父进程向管道发送数据
for content in ["聂风", "步惊云", "孔慈"]:
    conn2.send(content)
# 关闭父进程的发送
conn2.close()
p.join()
