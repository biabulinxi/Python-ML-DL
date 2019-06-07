# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/9 15:04
# @File_name:02_double_link_list.py
# @IDE:PyCharm

"""
双链表代码实现
"""


# (elem, None)
class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """
    ----------链表----------
    is_empty() 链表是否为空
    length() 链表长度
    travel() 遍历整个链表
    add(item) 链表头部添加元素
    append(item) 链表尾部添加元素
    insert(pos, item) 指定位置添加元素
    remove(item) 删除节点
    search(item) 查找节点是否存在
    """

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        # 游标移动
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('')

    def add(self,item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """
        指定位置添加元素
        :param pos ：从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 当循环退出后，cur指向pos的位置
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node


    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur != None:
            cur = cur.next
            if cur.elem == item:
                # 判断是否为头结点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.prev:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                    cur.prev = None
                    cur.next = None
                break

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return cur.elem
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    double_obj = DoubleLinkList()
    print(double_obj.is_empty())
    print(double_obj.length())

    double_obj.append(1)
    print(double_obj.is_empty())
    print(double_obj.length())

    double_obj.append(2)
    double_obj.travel()

    double_obj.add(8)
    double_obj.travel()

    double_obj.append(3)
    double_obj.append(4)
    double_obj.append(5)
    double_obj.travel()

    double_obj.insert(-1, 9)
    double_obj.travel()

    double_obj.insert(2, 100)
    double_obj.travel()

    double_obj.insert(10, 200)
    double_obj.travel()

    print(double_obj.search(200))

    double_obj.remove(200)
    double_obj.travel()
