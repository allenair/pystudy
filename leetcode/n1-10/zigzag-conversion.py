# -*- coding: utf-8 -*-
import functools


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        res = ["" for i in range(numRows)]

        pos = direct = 0
        for i in range(len(s)):
            res[pos] += s[i]
            if direct == 0:
                if pos == numRows - 1:
                    direct = 1
                    pos = pos - 1
                else:
                    pos = pos + 1
            else:
                if pos == 0:
                    direct = 0
                    pos = pos + 1
                else:
                    pos = pos - 1

        return functools.reduce(lambda x, y: x + y, res)


print(Solution().convert("PAYPALISHIRING", 3))
