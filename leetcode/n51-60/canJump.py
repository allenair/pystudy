# -*- coding:utf-8 -*-
class Solution:
    def canJump(self, nums: [int]) -> bool:
        length = len(nums)
        if length <= 1:
            return True

        n = length - 1
        while n > 0:
            tmp = n - 1
            flag = False
            while tmp >= 0 and not flag:
                if nums[tmp] >= (n - tmp):
                    flag = True
                tmp = tmp - 1
            if not flag:
                return False
            n = n - 1
        return True


print(Solution().canJump([3, 2, 1, 0, 4]))
