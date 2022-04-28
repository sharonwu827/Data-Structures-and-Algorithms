class TreeNode:
    def __init__(self):
        self.val = val
        self.left = None
        self.right = None


# preorder
def preorder(self, root: TreeNode) -> List[int]:
    res = []
    def pre_traversal(node):
        if node == None:
            return
        res.append(node.val)  # 前序
        preorder_traverse(node.left)
        preorder_traverse(node.right)

    pre_traversal(root)
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
