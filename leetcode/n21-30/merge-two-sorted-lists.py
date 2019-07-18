# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        move = head
        while l1 and l2:
            if l1.val < l2.val:
                move.next = l1
                move = move.next
                l1 = l1.next
            else:
                move.next = l2
                move = move.next
                l2 = l2.next
        while l1:
            move.next = l1
            move = move.next
            l1 = l1.next
        while l2:
            move.next = l2
            move = move.next
            l2 = l2.next

        return head.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


def my_print(lst):
    while lst:
        print(
            lst.val,
            '->',
        )
        lst = lst.next


my_print(Solution().mergeTwoLists(l1, l2))
