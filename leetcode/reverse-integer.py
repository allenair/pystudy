# -*- coding: utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x > 0 else -1
        newx = x if x > 0 else -1*x
        res = 0
        while newx:
            res = res*10 + newx % 10
            newx = newx // 10

        if flag == 1 and res >= 1<<31 or flag == -1 and res > 1<<31:
            return 0

        return flag*res


print(Solution().reverse(1563847412))

