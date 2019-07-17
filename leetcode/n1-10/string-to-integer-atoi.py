# -*- coding: utf-8 -*-
import re


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        m = re.match(r'^[-+]?\d+', str.strip())
        res = 0
        if m:
            res = int(m.group(0))
            if res >= 1 << 31:
                return (1 << 31)-1
            elif res*-1 >= 1 << 31:
                return -1 * (1 << 31)

        return res


print(Solution().myAtoi("2147483648"))
