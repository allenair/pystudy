# -*- coding: utf-8 -*-
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        num_arr = sorted(nums)

        for i in range(len(num_arr) - 3):
            if i > 0 and num_arr[i - 1] == num_arr[i]:
                continue
            three_res = self.threeSum(num_arr[i + 1:], target - num_arr[i])
            for _, lst in enumerate(three_res):
                lst.append(num_arr[i])
                res.append(lst)

        return res

    def threeSum(self, num_arr, target):
        res = []
        for i in range(len(num_arr) - 1):
            if i > 0 and num_arr[i - 1] == num_arr[i]:
                continue
            j, k = i + 1, len(num_arr) - 1
            while j < k:
                if num_arr[i] + num_arr[j] + num_arr[k] == target:
                    res.append([num_arr[i], num_arr[j], num_arr[k]])
                    j, k = j + 1, k - 1
                    while j < k and num_arr[j] == num_arr[j - 1]:
                        j = j + 1
                    while j < k and num_arr[k] == num_arr[k + 1]:
                        k = k - 1

                elif num_arr[i] + num_arr[j] + num_arr[k] < target:
                    j = j + 1
                else:
                    k = k - 1

        return res


print(Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))
