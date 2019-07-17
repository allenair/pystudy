# -*- coding: utf-8 -*-


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        res = s[0]

        dp = [[False for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s)):
            for k in range(i+1):
                if i-k <= 1 and s[i] == s[k]:
                    dp[k][i] = True
                elif s[i] == s[k] and dp[k+1][i-1]:
                    dp[k][i] = True

                if dp[k][i] and i-k+1 > len(res):
                    res = s[k:i+1]
        return res


print(Solution().longestPalindrome("babad"))
