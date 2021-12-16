def BFS(self):
    cur_node = self.root
    queue=[]
    res=[]
    # append entire node, the value and the left and the right
    queue.append(cur_node)
    while len(queue)>0:
        cur_node = queue.pop(0)
        res.append(cur_node.value)
        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)
    return results






