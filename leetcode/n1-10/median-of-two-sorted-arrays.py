# -*- coding: utf-8 -*-


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # a, b = sorted((nums1, nums2), key=len)
        m, n = len(nums1), len(nums2)

        pos1, pos2 = 0, 0
        if (m + n) % 2 == 0:
            pos1 = (m + n) // 2 - 1
            pos2 = pos1 + 1
        else:
            pos1 = (m + n + 1) // 2 - 1
            pos2 = pos1

        x = y = sum_two = 0
        for i in range(m + n):
            if x >= m:
                if sum_two == 0:
                    sum_two = nums2[pos1 - i + y]
                if pos1 == pos2:
                    sum_two = sum_two * 2
                else:
                    sum_two += nums2[pos1 - i + y + 1]
                break

            if y >= n:
                if sum_two == 0:
                    sum_two = nums1[pos1 - i + x]
                if pos1 == pos2:
                    sum_two = sum_two * 2
                else:
                    sum_two += nums1[pos1 - i + x + 1]
                break

            if nums1[x] < nums2[y]:
                now = nums1[x]
                x += 1
            else:
                now = nums2[y]
                y += 1

            if i == pos1:
                sum_two += now
                if pos2 == pos1:
                    sum_two = sum_two * 2
                    break
            if i == pos2:
                sum_two += now
                break

        return sum_two / 2.0


print(Solution().findMedianSortedArrays([1, 2], [3, 5]))
# print((2 + 2) // 2)
