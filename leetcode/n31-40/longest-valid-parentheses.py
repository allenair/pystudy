# -*- coding: utf-8 -*-


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == ')':
                stack.pop()
                if len(stack) > 0:
                    count = max(count, i - stack[-1])
                else:
                    stack.append(i)

            else:
                stack.append(i)

        return count

    def longestValidParentheses_dp(self, s):
        if not s:
            return 0

        dp = [0] * len(s)
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '(' and i + 1 + dp[i + 1] < len(s) and s[i + 1 + dp[i + 1]] == ')':
                dp[i] = dp[i + 1] + 2
                if i + 1 + dp[i + 1] + 1 < len(s):
                    dp[i] = dp[i] + dp[i + 1 + dp[i + 1] + 1]

        return max(dp)


# )(()))()
print(Solution().longestValidParentheses(")(()))()"))
print(Solution().longestValidParentheses_dp(")(()))()"))
