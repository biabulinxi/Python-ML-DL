# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/9 16:10
# @File_name:03_single_cycle_link_list.py
# @IDE:PyCharm

"""
单向循环链表实现
"""


# (elem, None)
class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
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
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 1
        # 游标移动
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环，但尾节点没有打印,需跳出循环打印
        print(cur.elem)

    def add(self,item):
        """链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        # cur游标，用来移动遍历节点
        cur = self.__head
        # 游标移动
        while cur.next != self.__head:
            cur = cur.next
        # 找到尾节点
        node.next = self.__head
        self.__head = node
        cur.next = self.__head

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

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
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 当循环退出后，cur指向pos-1的位置
            node.next = cur.next
            cur.next = node


    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return None
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
            if cur.next.elem == item:
                # 判断是否为头结点
                if cur == self.__head:
                    # 找尾节点
                    tail = self.__head
                    while tail.next != self.__head:
                        tail = tail.next

                    self.__head = cur.next
                    tail.next = self.__head
                else:
                    cur.next = cur.next.next
                return
        # 尾节点判断
        if cur.elem == item:
            if cur == self.__head:
                # 只有一个节点判断
                self.__head = None
        else:
            cur.next = cur.next.next


    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return cur.elem
            else:
                cur = cur.next
        # 退出循环,判断尾节点
        if cur.elem == item:
            return cur.elem
        return False


if __name__ == '__main__':
    single_obj = SingleLinkList()
    print(single_obj.is_empty())
    print(single_obj.length())

    single_obj.append(1)
    print(single_obj.is_empty())
    print(single_obj.length())

    single_obj.append(2)
    single_obj.travel()

    single_obj.add(8)
    single_obj.travel()
    #
    single_obj.append(3)
    single_obj.append(4)
    single_obj.append(5)
    single_obj.travel()

    single_obj.insert(-1, 9)
    single_obj.travel()

    single_obj.insert(2, 100)
    single_obj.travel()

    single_obj.insert(10, 200)
    single_obj.travel()

    print(single_obj.search(200))

    single_obj.remove(3)
    single_obj.travel()
