# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/9 17:57
# @File_name:03_dequeue.py
# @IDE:PyCharm

"""
双端队列的实现
"""

class Queue(object):
    """
    ----------双端队列---------
    Queue() 创建一个空的队列
    enqueue(item) 往队列中添加一个item元素
    dequeue() 从队列头部删除一个元素
    is_empty() 判断一个队列是否为空
    size() 返回队列的大小
    """

    def __init__(self):
        self.__list = []

    def add_front(self,item):
        """往队列头部中添加一个item元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """往队列尾部中添加一个item元素"""
        self.__list.append(item)

    def pop_front(self):
        """从队列头部取一个元素"""
        return self.__list.pop()

    def pop_rear(self):
        """从队列尾部取一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        return not self.__list

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()

