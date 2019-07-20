# -*- coding: utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = None
        i = 0
        while i < len(nums):
            if nums[i] == tmp:
                del (nums[i])
            else:
                tmp = nums[i]
                i = i + 1

        return len(nums)


print(Solution().removeDuplicates([1, 1, 2]))
