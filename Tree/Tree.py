class Node(value):
    def __init__(self):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def print_tree(self):

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        p = self.root
        while True:
            if new_node.value < p.value:
                if p.left is None:
                    p.left = new_node
                    return True
                else:
                    p = p.left
            elif new_node.value > p.value:
                if p.right == None:
                    p.right = new_node
                    return True
                else:
                    p = p.right
            else:  # elif new_node.value == p.value:
                return False

    def contain(self, value):
        if self.root is None:
            return False
        p = self.root
        while p:
            if value < p.value:
                p = p.left
            elif value > p.value:
                p = p.right
            else:
                return True
        return False

my_tree = BST()
my_tree.insert(2)
my_tree.insert(6)
