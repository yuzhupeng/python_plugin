#链表中每一个元素都是一个对象，每一个对象被称为节点，包含有数据域value和指向下一个节点的指针next。

#通过各个节点直接的相互链接，最终串成一个链表。
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class LinkedList(object):
    def __init__(self, size=None):
        """
        :param size: int or None, 如果None，则该链表可以无限扩充
        """
        self.size = size
        # 定义一个根节点
        self.root = Node()
        # 尾节点始终指向最后一个节点
        self.tail_node = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        # size 不为 None, 且长度大于等于size则链表已满
        if self.size and len(self) >= self.size:
            raise Exception("LinkedList is full")
        # 构建节点
        node = Node(value)
        tail_node = self.tail_node
        # 判断尾节点是否为空
        if tail_node is None:
            # 还没有 append 过，length = 0， 追加到 root 后
            self.root.next = node
        else:
            # 否则追加到最后一个节点的后边，并更新最后一个节点是 append 的节点
            tail_node.next = node
        # 把尾节点指向node
        self.tail_node = node
        # 长度加一
        self.length += 1

    # 往左边添加
    def append_left(self, value):
        if self.size and len(self) >= self.size:
            raise Exception("LinkedList is full")
        # 构建节点
        node = Node(value)
        # 链表为空，则直接添加设置
        if self.tail_node is None:
            self.tail_node = node

        # 设置头节点为根节点的下一个节点
        head_node = self.root.next
        # 把根节点的下一个节点指向node
        self.root.next = node
        # 把node的下一个节点指向原头节点
        node.next = head_node
        # 长度加一
        self.length += 1

    # 遍历节点
    def iter_node(self):
        # 第一个节点
        current_node = self.root.next
        # 不是尾节点就一直遍历
        while current_node is not self.tail_node:
            yield current_node
            # 移动到下一个节点
            current_node = current_node.next
        # 尾节点
        if current_node is not None:
            yield current_node

    # 实现遍历方法
    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    # 删除指定元素
    def remove(self, value):
        # 删除一个值为value的节点，只要使该节点的前一个节点的next指向该节点的下一个
        # 定义上一个节点
        perv_node = self.root
        # 遍历链表
        for current_node in self.iter_node():
            if current_node.value == value:
                # 把上一个节点的next指向当前节点的下一个节点
                perv_node.next = current_node.next
                # 判断当前节点是否是尾节点
                if current_node is self.tail_node:
                    # 更新尾节点 tail_node
                    # 如果第一个节点就找到了，把尾节点设为空
                    if perv_node is self.root:
                        self.tail_node = None
                    else:
                        self.tail_node = perv_node
                # 删除节点，长度减一，删除成功返回1
                del current_node
                self.length -= 1
                return 1
            else:
                perv_node = current_node
        # 没找到返回-1
        return -1

    # 查找元素，找到返回下标，没找到返回-1
    def find(self, value):
        index = 0
        # 遍历链表，找到返回index,没找到返回-1
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    # 删除第一个节点
    def popleft(self):
        # 链表为空
        if self.root.next is None:
            raise Exception("pop from empty LinkedList")
        # 找到第一个节点
        head_node = self.root.next
        # 把根节点的下一个节点，指向第一个节点的下一个节点
        self.root.next = head_node.next
        # 获取删除节点的value
        value = head_node.value
        # 如果第一个节点是尾节点, 则把尾节点设为None
        if head_node is self.tail_node:
            self.tail_node = None

        # 长度减一，删除节点，返回该节点的值
        self.length -= 1
        del head_node
        return value

    # 清空链表
    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.tail_node = None
        self.length = 0

    # 反转链表
    def reverse(self):
        # 第一个节点为当前节点，并把尾节点指向当前节点
        current_node = self.root.next
        self.tail_node = current_node
        perv_node = None

        while current_node:
            # 下一个节点
            next_node = current_node.next
            # 当前节点的下一个节点指向perv_node
            current_node.next = perv_node

            # 当前节点的下一个节点为空，则把根节点的next指向当前节点
            if next_node is None:
                self.root.next = current_node

            # 把当前节点赋值给perv_node
            perv_node = current_node
            # 把下一个节点赋值为当前节点
            current_node = next_node