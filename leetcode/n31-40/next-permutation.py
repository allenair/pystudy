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
            if nums[i] > nums[i - 1]:
                for k in range(len(nums)-1, i-1, -1):
                    if nums[k] > nums[i - 1]:
                        nums[i - 1], nums[k] = nums[k], nums[i - 1]
                        break
                for n in range(i, len(nums) - 1):
                    for m in range(n + 1, len(nums)):
                        nums[n], nums[m] = nums[m], nums[n]
                return nums
        else:
            nums.reverse()

        return nums


print(Solution().nextPermutation([1,3,2]))
print(Solution().nextPermutation([1,2,3]))
print(Solution().nextPermutation([4,2,0,2,3,2,0]))