class TreeNode:
    def __init__(self):
        self.val = val
        self.left = None
        self.right = None

    # https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html
    # 为了让递归的过程中的同一层的节点放在同一个列表中，在递归时要记录深度 depth
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(root, depth):
            if not root:
                return
            # start the current depth
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        # dfs(root, 0)
        # return res

# preorder
def preorder(self, root: TreeNode) -> List[int]:
    res = []

    def dfs(node):
        if node == None:
            return
        res.append(node.val)  # 前序
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res


# inorder
def inorder(root):
    res = []

    def inorder_traversal(node):
        if not node:
            return None
        inorder_traversal(node.left)
        res.appned(node.val)
        inorder_traversal(node.right）
        return res
    return inorder_traversal(root)


def postorder(root):
    res = []

    def postorder_traversal(node):
        if node == None:
            return
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        res.appned(node.val)

    postorder_traversal(root)
    return res
