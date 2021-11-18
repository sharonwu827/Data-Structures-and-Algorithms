## we use to linkedlist to construct the stack

class Node(value):
    def __init__(self):
        self.value = value
        self.next = None

class stack:
    def __init__(self,value):
        new_node = Node(value)
        self.head= new_node
        self.length = 1

    def print_stack(self):
        p = self.head
        for _ in self.length:
            print p.value
            p = p.next

    def push(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            # self.next = None
        else:
            new_node.next = self.head
            self.head =  new_node
        self.length+=1
        return True

    def pop(self):





my_stack = stack(4)
my_stack.print_stack()
