# Depth First Traversals:
# (a) Inorder (Left, Root, Right) : 4 2 5 1 3
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1
# Breadth-First or Level Order Traversal: 1 2 3 4 5


# Breadth First Search
def BFS(self):
    cur_node = self.root
    queue = []
    res = []
    # append entire node, the value and the left and the right
    queue.append(cur_node)
    while len(queue) > 0:
        cur_node = queue.pop(0)
        res.append(cur_node.value)
        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)
    return res


# Depth First Traversals
# PREORDER
def dfs_preorder(self):
    res = []
    def preorder_traverse(cur_node):
        res.append(cur_node.value)
        if cur_node.left is not None:
            preorder_traverse(cur_node.left)
        if cur_node.right is not None:
            preorder_traverse(cur_node.right)
    preorder_traverse(self.root)
    return res


# POSTORDER
def dfs_postorder(self):
    res = []
    def postorder_traverse(cur_node):
        if cur_node.left is not None:
            postorder_traverse(cur_node.left)
        if cur_node.right is not None:
            postorder_traverse(cur_node.right)
        res.append(cur_node.value)
    postorder_traverse(self.root)
    return res


# INORDER
def dfs_inorder(self):
    res = []
    def inorder_traverse(cur_node):
        if cur_node.left is not None:
            inorder_traverse(cur_node.left)
        res.append(cur_node.value)
        if cur_node.right is not None:
            inorder_traverse(cur_node.right)
        res.append(cur_node.value)
    inorder_traverse(self.root)
    return res
