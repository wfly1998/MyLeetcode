# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        extra = (l1.val + l2.val) // 10
        l = ListNode((l1.val + l2.val) % 10)
        cur = l
        while l1.next or l2.next or extra:
            v = extra
            if l1.next:
                l1 = l1.next
                v += l1.val
            if l2.next:
                l2 = l2.next
                v += l2.val
            extra = v // 10
            v %= 10
            cur.next = ListNode(v)
            cur = cur.next
        return l
            
if __name__ == '__main__':
    a = ListNode(2)
    a.next = ListNode(4)
    a.next.next = ListNode(3)
    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(4)
    sol = Solution()
    res = sol.addTwoNumbers(a, b)
    print(res.val)
    print(res.next.val)
    print(res.next.next.val)

