# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fake = ListNode(0)
        fake.next = head
        del_pt = tail_pt = fake

        while n and tail_pt:
            n = n - 1
            tail_pt = tail_pt.next

        while tail_pt.next:
            tail_pt = tail_pt.next
            del_pt = del_pt.next

        del_pt.next = del_pt.next.next

        return fake.next


myList = ListNode(1)
myList.next = ListNode(2)
myList.next.next = ListNode(3)
myList.next.next.next = ListNode(4)
myList.next.next.next.next = ListNode(5)


def my_print(lst):
    while lst:
        print(lst.val, '->')
        lst = lst.next


my_print(Solution().removeNthFromEnd(myList, 2))
