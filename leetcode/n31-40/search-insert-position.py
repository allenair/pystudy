# -*- coding: utf-8 -*-


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i
        else:
            return len(nums)


print(Solution().searchInsert([1, 3, 5, 6], 4))
