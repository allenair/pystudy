# -*- coding: utf-8 -*-


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num_arr = sorted(nums)

        min_val = 1 << 31

        for i in range(len(num_arr) - 2):
            if i > 0 and num_arr[i - 1] == num_arr[i]:
                continue
            j, k = i + 1, len(num_arr) - 1

            while j < k:
                temp = num_arr[i] + num_arr[j] + num_arr[k]
                if abs(temp - target) < abs(min_val - target):
                    min_val = temp
                if temp > target:
                    k = k - 1
                else:
                    j = j + 1

        return min_val


print(Solution().threeSumClosest([0, 2, 1, -3], 1))
