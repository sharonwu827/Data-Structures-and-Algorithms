
class ListNode(object):
    def __init__(self,value):
        self.value = value
        self.nextnode=None

#create nodes
a=ListNode(1)
b=ListNode(2)
c=ListNode(3)

print (a)

# link those nodes together
a.nextnode = b
b.nextnode = c


a.value # return 1
a.nextnode # return type
a.nextnode.value # return 2