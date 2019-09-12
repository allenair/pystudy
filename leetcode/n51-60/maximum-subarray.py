# -*- coding: utf-8 -*-


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nowMax, resMax = nums[0], nums[0]
        for i in range(1, len(nums)):
            nowMax = max(nowMax + nums[i], nums[i])
            resMax = max(resMax, nowMax)
        return resMax


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
