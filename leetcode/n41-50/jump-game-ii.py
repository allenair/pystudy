# -*- coding: utf-8 -*-


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        在争取每跳最远的greedy
        扫描数组，以确定当前最远能覆盖的节点，放入farest。
        然后继续扫描，直到当前的路程超过了上一次算出的覆盖范围，那么更新覆盖范围，同时更新条数，因为我们是经过了多一跳才能继续前进的
        """
        res, last, farest = 0, 0, 0
        for i in range(len(nums)):
            if i > last:
                res += 1
                last = farest
            farest = max(farest, nums[i] + i)
        return res


print(Solution().jump([2, 3, 1, 1, 4]))
