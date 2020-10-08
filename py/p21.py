class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_node = None
        cur_node = None
        while l1 and l2:
            min_node = l1
            if l2.val < min_node.val:
                min_node = l2
                l2 = l2.next
            else:
                l1 = l1.next

            if cur_node:
                cur_node.next = min_node
                cur_node = min_node
            if not new_node:
                new_node = min_node
                cur_node = min_node
        if not new_node:
            new_node = l1 if l1 else l2
        if cur_node:
            cur_node.next = l1 if l1 else l2
        return new_node
