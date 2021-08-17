class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
## create single linked list
class Slinkedlist:
    def __init__(self):
        self.head=None  ## --- O(1)
        self.tail=None  ## --- O(1)
singlyLinkedlist = Slinkedlist()
node1=Node(1)
node2=Node(2)

singlyLinkedlist.head=node1
singlyLinkedlist.head.next=node2   ## --- O(1)
singlyLinkedlist.tail = node2


## insertion

