# -*- coding: utf-8 -*-
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for _, c in enumerate(s):
            if c == '}' or c == ')' or c == ']':
                if not stack:
                    return False
                if c == '}' and stack.pop() != '{' or c == ')' and stack.pop() != '(' or c == ']' and stack.pop() != '[':
                    return False
            else:
                stack.append(c)

        return not stack


print(Solution().isValid('(}'))
