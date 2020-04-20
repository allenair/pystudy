# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pos = 0
        arr = s.split()
        if len(arr) > 0:
            pos = len(arr[-1])

        return pos

print(Solution().lengthOfLastWord('Hello World'))
