# Python does not have linked lists in its standard library.
# We implement the concept of linked lists using the concept of nodes

# Creation of Node
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext

temp = Node(93)
temp.getData()











# Creation of Linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    # To insert an element in a linked list at the beginning
    # we will first create a node and with the given data and assign its next reference to the first node
    # i.e where the head is pointing.
    # then we point the head reference to the new node.

    def insertAtBeginning(self, data):
        temp = Node(data) # first create a node with given data
        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head # assign the value's next reference to the first node
            self.head = temp

    # To insert an element in a linked list at the end
    # we just have to find the node where the next element refers to None i.e. the last node.
    # Then we create a new node with the given data and point the next element of the last node to the newly created node.

    def insertAtEnd(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = temp

    # To insert an element at any other given position
    # we can count the nodes till we reach that position
    # then we point the next element of the new node to the next node of the current node
    # the next reference of the current node to the new node.

    def insertAtGivenPosition(self, data, position):
        count = 1
        curr = self.head # start from the head
        while count < position - 1 and curr != None:
            curr = curr.next
            count += 1
        temp = Node(data)
        temp.next = curr.next
        curr.next = temp

    # To traverse a linked list in python
    # we will start from the head, print the data and move to the next node until we reach None i.e. end of the linked list.
    # The following traverse() method implements the program to traverse a linked list in python.

    def traverse(self):
        curr = self.head # start from the head
        while curr != None: # until we reach the end
            print(curr.data)
            curr = curr.next


    # To delete the first node of a linked list
    # we will first check if the head of the linked list is pointing to None
    # if yes then we will raise an exception hat the linked list is empty
    # Otherwise, we will delete the current node referred by head and move the head pointer to the next node.
    def delFromBeginning(self):
        try:
            if self.head == None:
                raise Exception("Empty Linked List")
            else:
                temp = self.head
                self.head = self.head.next # move the head pointer to the next node
                del temp
        except Exception as e:
            print(str(e))

    # To delete the last node of the linked list
    # we will traverse each node in the linked list
    # check if the next pointer of the next node of current node points to None
    # if yes then the next node of current node is the last node and it will get deleted.

    def delFromEnd(self):
        try:
            if self.head == None:
                raise Exception("Empty Linked List")
            else:
                curr = self.head
                prev = None
                while curr.next != None:
                    # traverse each node in the linked list
                    prev = curr
                    curr = curr.next
                prev.next = curr.next
                del curr
        except Exception as e:
            print(str(e))


    def delAtPos(self, position):
        try:
            if self.head == None:
                raise Exception("Empty Linked List")
            else:
                curr = self.head
                prev = None
                count = 1
                while curr != None and count < position:
                    prev = curr
                    curr = curr.next
                    count += 1
                prev.next = curr.next
                del curr
        except Exception as e:
            print(str(e))