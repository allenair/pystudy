# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        pos = res
        carry = 0
        while l1 and l2:
            sum, carry = self.deal_carry(l1.val + l2.val, carry)
            pos.next = ListNode(sum)
            l1 = l1.next
            l2 = l2.next
            pos = pos.next

        while l1:
            sum, carry = self.deal_carry(l1.val, carry)
            pos.next = ListNode(sum)
            l1 = l1.next
            pos = pos.next

        while l2:
            sum, carry = self.deal_carry(l2.val, carry)
            pos.next = ListNode(sum)
            l2 = l2.next
            pos = pos.next

        if carry > 0:
            pos.next = ListNode(carry)

        return res.next

    def deal_carry(self, sum, carry):
        sum = sum + carry
        if sum > 9:
            sum = sum - 10
            carry = 1
        else:
            carry = 0

        return sum, carry


def init_list(lst):
    res = ListNode(0)
    pos = res
    for i, val in enumerate(lst):
        pos.next = ListNode(val)
        pos = pos.next
    return res.next


def print_list(lst):
    while lst:
        print(lst.val)
        lst = lst.next


testl1 = init_list([1])
testl2 = init_list([9, 9])
testres = Solution().addTwoNumbers(testl1, testl2)

print_list(testres)
