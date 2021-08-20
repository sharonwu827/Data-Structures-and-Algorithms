

class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode=None
#create nodes
a=Node(1)
b=Node(2)
c=Node(3)

# link those nodes together
a.nextnode = b
b.nextnode = c


a.value # return 1
a.nextnode # return type
a.nextnode.value # return 2