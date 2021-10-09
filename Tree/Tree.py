
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
    return root


def insertRight(root,newbranch):
    t = root.pop(2)
    if len(t)>1:
        root.insert(1,[newbranch,[],t])
    else:
        root.insert(1,[newbranch,[],[]])
    return root

def getRootVal(root):
    return root[0]
def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChile(root):
    return root[2]


r = BinaryTree(3)

insertLeft(r,3)
insertRight(r,4)
