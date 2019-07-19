# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head

        res_lst = new_head = ListNode(0)
        first = head
        second = head.next

        while first and second:
            tmp1 = first.next.next
            if second.next:
                tmp2 = second.next.next
            else:
                tmp2 = None

            new_head.next = second
            new_head.next.next = first
            new_head = new_head.next.next
            first = tmp1
            second = tmp2

        if first:
            new_head.next = first
        else:
            new_head.next = None

        return res_lst.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(4)


def my_print(lst):
    while lst:
        print(lst.val, '->', end='')
        lst = lst.next


my_print(Solution().swapPairs(l1))