# -*- coding: utf-8 -*-


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle or haystack == needle:
            return 0

        index = -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return index


print(Solution().strStr("mississippi", 'pi'))
