class TreeNode:
    def __init__(self):
        self.val = val
        self.left = None
        self.right = None

# preorder
def preorder(root):
    stack = []
    res = []
    cur_node = root
    while stack or cur_node:
        if cur_node:
            res.append(cur_node.val)   #先访问根节点
            stack.append(cur_node)
            cur_node = cur_node.left
        else:
            cur_node = stack.pop() #回溯至父节点
            cur_node = cur_node.right
    return res

# inorder
def inorder(root):
    stack = []
    res = []
    cur_node = root
    while stack or root:
        if cur_node:
            stack.append(cur_node)
            cur_node = cur_node.left
        else:
            cur_node = stack.pop()
            res.append(cur_node.val)  # 左孩子先pop出来，再pop根节点
            cur_node = cur_node.right
    return res


def postorder(root):
    stack = []
    res = []
    cur_node = root
    while stack or root:
        if cur_node:
            res.append(cur_node.val)  # 先访问根节点
            stack.append(cur_node)
            cur_node = cur_node.right # 这从left变成了 right
        else:
            root = stack.pop()
            root = root.left  # 这从right变成了 left
    return res[::-1]




