#-*- coding: utf-8 -*-


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]

        tmp = self.find_pos(nums, target, 1)
        if tmp:
            res[0] = min(tmp)

        tmp = self.find_pos(nums, target, 2)
        if tmp:
            res[1] = max(tmp)
        return res

    def find_pos(self, nums, target, direct):
        res = []
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res.append(mid)
                if direct == 1:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return res


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
