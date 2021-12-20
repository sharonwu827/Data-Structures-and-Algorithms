# PREORDER

def dfs_preorder(self):
    res = []
    def traverse(cur_node):
        res.append(cur_node.value)
        if cur_node.left is not None:
            traverse(cur_node.left)
        if cur_node.right is not None:
            traverse(cur_node.right)
    traverse(self.root)
    return res


# POSTORDER

def dfs_postorder(self):
    res = []
    def traverse(cur_node):
        def traverse(cur_node):
            if cur_node.left is not None:
                traverse(cur_node.left)
            if cur_node.right is not None:
                traverse(cur_node.right)
            res.append(cur_node.value)

    traverse(self.root)
    return res


# INORDER










