class Node(value):
    def __init__(self):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_queue(self):
        p = self.head
        while p.next:
            print
            p.value
            p = p.next

    # enqueue: Push
    def Enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.tail
            temp.next = new_node
            self.tail = new_node
            # temp.next = None
        self.length += 1

    # Dequeue: pop
    def Dequeue(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length ==1:
            self.head = None
            temp.next = None
        else:
            self.head = temp.next
            temp.next = None
        self.length-=1
        return temp

my_queue = Queue(4)
