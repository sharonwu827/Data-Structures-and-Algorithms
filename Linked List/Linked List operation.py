class LinkList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverse(self):
        pre = LinkList(None)
        cur = head
        while cur:
            second = cur.next
            cur.next = pre
            pre = cur
            cur = second
        return pre

    def findMid(self):
        p1 = head
        p2 = head
        while p2:
            p1 = p1.next
            p2 = p2.next.next
        return p1

    def getLength(self):
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        return length


class solustion:
    def mergedTwoLists(l1, l2):
        dummy = ListNode(None)
        p = dummy
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return dummy.next