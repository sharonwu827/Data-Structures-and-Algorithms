# Python does not have linked lists in its standard library.
# We implement the concept of linked lists using the concept of nodes

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,vale):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # print a linkedlist
    def print_linkedlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    # append
    def append(self,value):
        new_node  = Node(value)
        if self.head is None: # self.length == 0
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length = 1

    def pop(self,value):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None: # temp.text
            pre = temp
            temp=temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length ==0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self, value):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None # remove the previous head from the linked list
        self.length -=1
        if self.length ==0:
            self.tail = None
        return temp

    def get(self,index): # return the node for the index
        if index <0 or index >=self.length:
            return None
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value): # change the value for the index
        new_node = Node(value)
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # at a particular index,insert a node
    def insert_node(self,index, value):
        if index <0 or index >=self.length:
            return False
        if index == 0:
            return self.prepend(value)
        elif index == length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length+=1
            return True

    # at a particular index, remove a node
    def remove_node(self, index):
        if index <0 or index >=self.length:
            return False
        if index == 0:
            return self.pop_first(value)
        elif index == length-1:
            return self.pop(value)
        else:
            temp = self.get(index-1)
            tem
            temp.next = temp.next.next
            temp.next = new_node
        self.length+=1
        return True













my_linked_list = LinkedList(4)
# print(my_linked_list.head.value)
