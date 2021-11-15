
class Node(value):
    def __init__(self):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        p = self.head
        while p:
            print p.value
            p = p.next
        return True

    def append(self,value):
        new_node = Node(value)
        if self.length == 0 :
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new.node.prev = self.tail
            self.tail = new_node
        self.length+=1
        return True

    def pop(self):
        if self.length == 0 :
            return None
        temp = self.tail
        before = temp.pre
        self.tail = before
        self.tail.next = None
        temp.prev = None
        self.length-=1
        if self.length==0:
            self.head = None
            self.tail =None
        retun temp

    def prepend(self):




