# -*- coding: utf-8 -*-


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        res = 0
        max_hight = max(height)

        for m in range(max_hight):
            left, right = 0, 0
            for i in range(len(height)):
                if height[i] > 0:
                    left = i
                    break

            for k in reversed(range(len(height))):
                if height[k] > 0:
                    right = k
                    break

            for n in range(len(height)):
                if height[n] == 0:
                    if left < n < right:
                        res += 1
                else:
                    height[n] -= 1

        return res

    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        res = 0
        left, right = 0, len(height) - 1
        left_wall, right_wall = 0, 0

        while left <= right:
            if left_wall <= right_wall:
                left_wall = max(left_wall, height[left])
                res += left_wall - height[left]
                left += 1
            else:
                right_wall = max(right_wall, height[right])
                res += right_wall - height[right]
                right -= 1
        return res


print(Solution().trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 3]))
