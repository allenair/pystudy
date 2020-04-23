# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmpSet = set()
        newList = ListNode(0)
        now = newList
        while head != None:
            if head.val not in tmpSet:
                tmpSet.add(head.val)
                now.next = ListNode(head.val)
                now = now.next

            head = head.next
        now.next = None

        return newList.next


a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
a.next = b
b.next = c
c.next = None
res = Solution().deleteDuplicates(a)
while res != None:
    print(res.val)
    res = res.next
