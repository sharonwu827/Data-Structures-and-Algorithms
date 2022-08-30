# Python does not have linked lists in its standard library.
# We implement the concept of linked lists using the concept of nodes

class Node(value):
    def __init__(self):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = None
        self.length = 1

    def print_list(self):
        p = self.head
        while p.next:
            print
            p.value
            p = p.next

    def append(self, value):
        new_node = Node(value)  # new node need to be appended
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        p = self.head
        pre = self.head
        while p.next:
            pre = p
            p = p.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # corner case when original linkedlist has only one node
        if self.length == 0:
            self.head = None
            self.tail = None
        return p

    def prepend(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True

    def pop_first(self):
        if self.length==0:
            return None
        else:
            p = self.head
            self.head = p.next
            p.next = None
        self.length-=1
        if self.length==0:
            self.tail = None
        return p

    # return the node of index
    def get(self,index): # index starts from 0
        if index < 0 or index >= self.length:
            return None
        p = self.head
        for _ in range(index):
            p = p.next
        return p

    def set_value(self,index,value):
        p = self.get(index)
        if p:
            p.value=value
            return True
        return False

    def insert(self,index,value):
        new_node = Node(value)
        if index<0 or index>=self.length:
            return False
        elif index ==0:
            return self.preappend(value)
        elif index == self.length-1:
            return self.append(value)
        else:
            pre = self.get(index-1)
            pre.next = new_node
            new_node.next = pre.next
        self.length+=1
        return True

    def remove(self,index):
        if index < 0 or index >= self.length:
            return False
        elif index ==0:
            return self.pop_first()
        elif index ==self.length-1:
            return self.pop()
        else:
            pre = self.get(index-1)
            post = pre.next # the node to be removed
            pre.next = post.next
            post.next = None
        self.length -= 1
        return True

    def reversed(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.reverse()
my_linked_list.print_list()


def reverse(head, tail):
    cur = head
    pre = None
    while cur!=tail:
        # 留下联系方式
        nxt = cur.next
        # 修改指针
        cur.next = pre
        # 继续往下走
        pre = cur
        cur = nxt

def dfs(head, pre):
    if not head:
        return pre
    # 留下联系方式（由于后面的都没处理，因此可以通过 head.next 定位到下一个）
    next = head.next
    # 主逻辑（改变指针）在进入后面节点的前面（由于前面的都已经处理好了，因此不会有环）
    head.next = pre
    dfs(next, head)
    return res




