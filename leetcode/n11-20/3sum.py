# -*- coding: utf-8 -*-


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        num_arr = sorted(nums)
        res = []
        for i in range(len(num_arr) - 1):
            if num_arr[i] > 0 :
                return res
            if i > 0 and num_arr[i - 1] == num_arr[i]:
                continue
            j, k = i + 1, len(num_arr) - 1
            while j < k:
                if num_arr[i] + num_arr[j] + num_arr[k] == 0:
                    res.append([num_arr[i], num_arr[j], num_arr[k]])
                    j, k = j + 1, k - 1
                    while j < k and num_arr[j] == num_arr[j - 1]:
                        j = j + 1
                    while j < k and num_arr[k] == num_arr[k + 1]:
                        k = k - 1

                elif num_arr[i] + num_arr[j] + num_arr[k] < 0:
                    j = j + 1
                else:
                    k = k - 1

        return res


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))