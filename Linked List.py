class ListNode(object):
    def __init__(self,value):
        self.value = value
        self.nextnode=None

#create nodes
a=ListNode(1)
b=ListNode(2)
c=ListNode(3)

print (a)

# link those nodes together
a.nextnode = b
b.nextnode = c


a.value # return 1
a.nextnode # return type
a.nextnode.value # return 2




# Deletion in Linked List
# below is the structure of a node which is used to create a new node every time

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #none is nothing but null

# creating a class for implementing the code for deletion in a linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Inserting at the end of a Linked List (append function)
    def append(self,key):
        h=self.head
        if h is None:
            new_node=Node(key)
            self.head = new_node
        else:
            while h.next != None:
                h=h.next
            new_node = Node(key)
            h.next=new_mode






