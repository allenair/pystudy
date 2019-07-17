# -*- coding utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for index, item in enumerate(nums):
            if target - item in d:
                return [d[target - item], index]
            d[item] = index

print(Solution().twoSum([2,7,11,15],9))
