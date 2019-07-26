# -*- coding: utf-8 -*-


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                tmpIndex = nums[i]
                nums[i], nums[tmpIndex - 1] = nums[tmpIndex - 1], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1

    def firstMissingPositive2(self, nums):
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
                
        for i in range(0, len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

print(Solution().firstMissingPositive([3, 4, -1, 1]))
