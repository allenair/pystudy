# -*- coding: utf-8 -*-
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        nums1.sort()


a = [1, 2, 3, 0, 0, 0]
b = [2, 5, 6]
Solution().merge(a, 3, b, 3)
print(a)