# -*- coding: utf-8 -*-


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums

        for i in range(len(nums) - 1, 0, -1):
            for k in range(i-1, -1, -1):
                if nums[i] > nums[k]:
                    nums[i], nums[k] = nums[k], nums[i]
                    for n in range(k+1, len(nums)-1):
                        for m in range(n+1, len(nums)):
                            nums[n], nums[m] = nums[m], nums[n]
                    return nums
        else:
            nums.reverse()

        return nums


print(Solution().nextPermutation([4,2,0,2,3,2,0]))
