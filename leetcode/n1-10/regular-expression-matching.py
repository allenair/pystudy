# -*- coding: utf-8 -*-

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n=len(s),len(p)
        dp=[[False] * (n+1) for _ in range(m+1)]

        dp[0][0]=True
        for j in range(1, n+1):
            dp[0][j] = j>1 and p[j-1]=='*' and dp[0][j-2]

        for i in range(1, m+1):
            for k in range(1, n+1):
                if p[k-1]=='*':
                    dp[i][k] = dp[i][k-2] or (s[i-1]==p[k-2] or p[k-2]=='.') and dp[i-1][k]
                else:
                    dp[i][k] = (p[k-1]=='.' or s[i-1]==p[k-1]) and dp[i-1][k-1]
        return dp[m][n]

print(Solution().isMatch("aaa","a*"))
