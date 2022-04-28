


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # iteration
    # iteration has better space complexity
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(None)
        cur = dummy
        while l1 and l2:
            if l1.val<l2.val:
                dummy.next = l1
            else:
                dummy.next = l2
        cur.next = l1 if l1 else l2
        return dummy.next

    # recursion
    def mergeTwoLists(self, l1, l2)
        dummy = ListNode(None)
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val<l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2



