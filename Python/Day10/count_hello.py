# @Project:AID1810
# @Author:biabu
# @Date:2018/11/14 11:50
# @File_name:count_hello.py
# @IDE:PyCharm



count = 0
def hello(name):
    print("你好,",name)
    global count
    count += 1

hello("小张") # 打印 ： 你 好 ， 小 张
hello("小李")  # 打印 ： 你 好 ， 小 李
print("hello这个函数被调用", count,'次')