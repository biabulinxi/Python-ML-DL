# @Project:AID1810
# @Author:biabu
# @Date:18-12-21 上午9:28
# @File_name:01_不能使用input.py
# @IDE:PyCharm


from multiprocessing import Process

def fun1():
    # multiprocessing 模块没有提供输入接口(不能使用inputh函数)
    name = input("Please input name")


# 使用Process类创建进程对象，并关联相关函数
p = Process(target=fun1)
# 通过进程对象启动进程（start( )），自动执行进程函数
p.start()

print("I am father thread")