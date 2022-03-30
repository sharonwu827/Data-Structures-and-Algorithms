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
        res.appned(node.val)  # 前序
        preorder_traverse(cur_node.left)
        preorder_traverse(cur_node.right)

    pre_traversal(root)
    return res


# inorder
def inorder(root):
    res = []

    def inorder_traversal(node):
        if node == None:
            return
        inorder_traversal(cur_node.left)
        res.appned(node.val)
        inorder_traversal(cur_node.right）

    inorder_traversal(root)
    return res


def postorder(root):
    res = []

    def postorder_traversal(node):
        if node == None:
            return
        postorder_traversal(cur_node.left)
        postorder_traversal(cur_node.right)
        res.appned(node.val

    postorder_traversal(root)
    return res


