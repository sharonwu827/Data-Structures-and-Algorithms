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
            print
            p.value
            p = p.next
        return True

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new.node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            before = temp.pre
            self.tail = before
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_head
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        # index in the first half of the list
        p = self.head
        if index < self.length / 2:
            for _ in range(index):
                p = p.next
        else:
            p = self.tail
            for _ in range(self.length - 1, index, -1):
                p = p.prev
        return p.value

    def set(self, index, value):
        while self.get(index):
            self.get(index).value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)

        if index < 0 or index >= self.length:
            return False

        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            before = self.get(index - 1)
            current = self.get(index)
            before.next = new_node
            new_node.prev = before
            new_node.next = current
            current.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get(index)
            temp.next.prev = temp.pre
            temp.pre.next = temp.next
            temp.prev = None
            temp.next = None
        self.length -= 1
        return temp
