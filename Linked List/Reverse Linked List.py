
class Solution:
    def reverseList(self, head):
        if not head:
            return None
        pre = None
        cur = head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre