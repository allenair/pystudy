# -*- coding: utf-8 -*-
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1 = str(x)
        x2 = x1[::-1]

        return x1 == x2


print(Solution().isPalindrome(-121))
