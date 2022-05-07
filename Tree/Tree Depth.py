class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def getHeight(self, node):
        if not node:
            return 0
        left = getHeight(node.left)+1
        right = getHeight(node.right) + 1
        return max(left, right)