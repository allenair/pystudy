# -*- coding: utf-8 -*-


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start = 0
        max_len = 0
        for index, val in enumerate(s):
            if val in d:
                start = max(start, d[val] + 1)
            d[val] = index
            max_len = max(max_len, index - start + 1)

        return max_len


print(Solution().lengthOfLongestSubstring("abba"))
