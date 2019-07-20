# -*- coding: utf-8 -*-


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            flag = -1
        dividend = dividend if dividend > 0 else -1 * dividend
        divisor = divisor if divisor > 0 else -1 * divisor

        ans = 0
        cnt = 1
        if divisor == 1:
            ans = dividend
            if flag==1 and ans == 1 << 31:
                return (1 << 31) - 1
            elif flag==-1 and ans==1 << 31:
                return -1 * (1<<31)
        else:
            subsum = divisor
            while dividend >= divisor:
                while (subsum << 1) <= dividend:
                    cnt <<= 1
                    subsum <<= 1
                ans += cnt
                cnt = 1
                dividend -= subsum
                subsum = divisor
                

        return ans * flag


print(Solution().divide(1,1))
