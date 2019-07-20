# -*- coding: utf-8 -*-
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        res_lst = new_head = ListNode(0)
        start = end = head
        while start:
            n = k - 1
            while end and n:
                end = end.next
                n = n - 1
            if not end:
                new_head.next = start
                break
            else:
                tmp = end.next
                end.next = None
                new_head.next = self.inner_reverse(start)
                while new_head.next:
                    new_head = new_head.next
                start = end = tmp

        return res_lst.next

    def inner_reverse(self, lnk):
        stack = []
        res = head = ListNode(0)
        while lnk:
            stack.append(lnk)
            lnk = lnk.next

        while stack:
            head.next = stack.pop()
            head = head.next

        head.next = None
        return res.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)


def my_print(lst):
    while lst:
        print(lst.val, '->', end='')
        lst = lst.next


# my_print(Solution().inner_reverse(l1))

my_print(Solution().reverseKGroup(l1, 2))