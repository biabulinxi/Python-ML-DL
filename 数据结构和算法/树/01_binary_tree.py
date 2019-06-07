# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/10 10:50
# @File_name:01_binary_tree.py
# @IDE:PyCharm

"""
二叉树实现:节点表示以及树的创建
"""

class Node():
    """二叉树节点,通过使用Node类中定义三个属性，分别为elem本身的值，还有lchild左孩子和rchild右孩子"""

    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree():
    """二叉树,树的创建,创建一个树的类，并给一个root根节点，一开始为空，随后添加节点"""

    def __init__(self):
        self.root = None

    def add(self, item):
        """广度优先遍历进行添加元素"""
        node = Node(item)
        if self.root is None:  # 判断树的根节点是否为空
            self.root = node
            return
        queue = [self.root]  # 用来存放待处理的数据,利用队列进行操作
        while queue:
            cur_node = queue.pop(0)  #获取当前节点
            # 判断左右子节点
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历"""

        if self.root is None:
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        """先序遍历: 根节点 --> 左子节点 --> 右子节点 递归处理"""
        if node is None:  # 递归终止条件
            return
        print(node.elem, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """中序遍历: 左子节点 --> 根节点 --> 右子节点 递归处理"""
        if node is None:  # 递归终止条件
            return
        self.inorder(node.lchild)
        print(node.elem, end=' ')
        self.inorder(node.rchild)

    def postorder(self, node):
        """后序遍历: 左子节点 --> 右子节点 --> 根节点 递归处理"""
        if node is None:  # 递归终止条件
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=' ')


if __name__ == '__main__':
    binary_tree = Tree()
    binary_tree.add(0)
    binary_tree.add(1)
    binary_tree.add(2)
    binary_tree.add(3)
    binary_tree.add(4)
    binary_tree.add(5)
    binary_tree.add(6)
    binary_tree.add(7)
    binary_tree.add(8)
    binary_tree.add(9)

    binary_tree.breadth_travel()
    print('\n')
    binary_tree.preorder(binary_tree.root)
    print('\n')
    binary_tree.inorder(binary_tree.root)
    print('\n')
    binary_tree.postorder(binary_tree.root)
