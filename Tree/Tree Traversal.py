# Breadth First Search
def BFS(self):
    cur_node = self.root
    queue = []
    res = []
    # append entire node, the value and the left and the right
    queue.append(cur_node)
    while queue:
        cur_node = queue.pop(0)
        res.append(cur_node.value)
        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)
    return res


# Depth First Traversals
# Preorder recursion
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    def preorder_traverse(cur_node):
        if node is not None:
            res.append(cur_node.value)
            if cur_node.left is not None:
                preorder_traverse(cur_node.left)
            if cur_node.right is not None:
                preorder_traverse(cur_node.right)
    preorder_traverse(self.root)
    return res

# Preorder iteration
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    stack = []
    cur_node = root
    while stack or cur_node:
        while cur_node:
            stack.append(cur_node)
            res.append(cur_node.val)
            cur_node = cur_node.left
        cur_node = stack.pop()
        cur_node = cur_node.right
    return res




# Postorder recurison
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    def dfs(node):
        if node is not None:
            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)
            res.append(node.val)

    dfs(root)
    return res


# Postorder iteration
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    stack = [root]
    while stack:
        cur_node =stack.pop()
        res.append(cur_node.val)
        if cur_node.left:
            stack.append(cur_node.left)
        if cur_node.right:
            stack.append(cur_node.right)
    return res[::-1]


# inorder recursion
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    if not root:
        return None

    def traveral(node):
        if node.left is not None:
            traveral(node.left)
        res.append(node.val)
        if node.right is not None:
            traveral(node.right)

    traveral(root)
    return res

# inorder iteration
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    stack = []
    cur_node = root
    if not root:
        return None
    while stack or cur_node:
        while cur_node:
            stack.append(cur_node)
            cur_node = cur_node.left
        cur_node = stack.pop()
        res.append(cur_node.val)
         cur_node = cur_node.right
    return res


# Depth First Traversals Iteration
# PREORDER
def dfs_preorder(self):
    cur_node = self.root
    stack = [cur_node]
    res = []
    while stack:
        # First get the root element from the stack by popping the last element
        cur_node = stack.pop()
        # if the root is not None, we will append in the res
        if cur_node is not None:
            res.append(cur_node.val)
            # we will insert the right and then left element in the stack
            if cur_node.right is not None:
                stack.append(cur_node.right)
            # then left so that it is the last element in the stack
            # because in preorder we need the root node first then left and then right
            if cur_node.left is not None:
                stack.append(cur_node.left)
    return res
