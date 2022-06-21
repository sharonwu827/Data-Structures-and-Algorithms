class TreeNode:
    def __init__(self):
        self.val = val
        self.left = None
        self.right = None

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        queue = [root]
        res = []
        while queue:
            temp = []
            # 层内遍历 遍历当前层的所有节点 如果要确定当前遍历到了哪一层
            for _ in range(len(queue)):
                cur = queue.pop(0)
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(temp)
        return res

    # preorder
    def preorder(root):
        stack = []
        res = []
        cur_node = root
        while stack or cur_node:
            if cur_node:
                res.append(cur_node.val)  # 先访问根节点
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()  # 回溯至父节点
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
            cur_node = cur_node.right  # 这从left变成了 right
        else:
            cur = stack.pop()
            cur = cur.left  # 这从right变成了 left
    return res[::-1]
