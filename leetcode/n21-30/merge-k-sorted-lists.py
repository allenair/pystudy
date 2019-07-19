# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for _, lst in enumerate(lists):
            while lst:
                res.append(lst.val)
                lst = lst.next

        res.sort()

        head = tail = ListNode(0)
        for _, num in enumerate(res):
            tail.next = ListNode(num)
            tail = tail.next

        return head.next


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)


def my_print(lst):
    while lst:
        print(lst.val, '->', end='')
        lst = lst.next

my_print(Solution().mergeKLists([l1, l2, l3]))
