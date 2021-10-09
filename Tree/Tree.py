
### Tree representation (lists)

def BinearyTree(r):
    '''
    :param r: root node
    :return: two empty sublists
    '''
    return [r,[],[]]

def insertLeft(root,newbranch):
    t = root.pop(1)
    if len(t)>1:
        root.insert(1,[newbranch,t,[]])
    else:
        root.insert(1,[newbranch,[],[]])
        root.insert(1, [newbranch, [], []])
    return root

