# -*- coding: utf-8 -*-


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        n = 13，13在二进制中表示为：00001101，那么13 = 2^3 + 2^2 + 2^0
        """
        if not x:
            return 0.0
        if not n:
            return 1.0

        res = 1.0
        x = x if n > 0 else 1 / x
        n = abs(n)

        while n:
            if n & 1:
                res = res * x
            x = x * x
            n = n >> 1

        return res


print(Solution().myPow(2.00000, 15))