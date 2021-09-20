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

    # Utility function to print the linked list
    def printList(self):
        h=self.head
        while h :
            print(h.data, end=" ")
            h=h.next
        print()

    # deleting a given node
    def deleteNode(self, key):
        h=self.head
        prev=None
        if h is None:
            print("the list is empty")
            return

        if h.data ==key:
            self.head = h.next
            return

        while h is not None and h.data!=key:
            prev = h
            h=h.next
        if h is None:
            print ("key is not in the list")
        prev.next = h.next


# Code execution starts here
if __name__=='__main__':

	myList = LinkedList()
	myList.append(3)
	myList.append(4)
	myList.append(5)
	myList.append(6)
	myList.append(7)
	myList.append(9)
	print("Original List is: ", end = " ")
	myList.printList()
	myList.deleteNode(6)
	print("After Deletion: ", end = " ")
	myList.printList()










