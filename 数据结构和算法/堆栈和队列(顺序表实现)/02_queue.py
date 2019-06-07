# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/9 17:48
# @File_name:02_queue.py
# @IDE:PyCharm

"""
队列的实现
"""

class Queue(object):
    """
    ----------队列---------
    Queue() 创建一个空的队列
    enqueue(item) 往队列中添加一个item元素
    dequeue() 从队列头部删除一个元素
    is_empty() 判断一个队列是否为空
    size() 返回队列的大小
    """

    def __init__(self):
        self.__list = []

    def enqueue(self,item):
        """往队列中添加一个item元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        return not self.__list

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
