# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/9 17:32
# @File_name:01_stack.py
# @IDE:PyCharm

"""顺序表数据存储实现堆栈操作"""

class Stack(object):
    """
    -----------堆栈-------------
    Stack() 创建一个新的空栈
    push(item) 添加一个新的元素item到栈顶
    pop() 弹出栈顶元素
    peek() 返回栈顶元素
    is_empty() 判断栈是否为空
    size() 返回栈的元素个数
    """

    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return not self.__list

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
