# -*- coding: utf-8 -*-
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        finLst = []
        self.DFS(n, n, '', finLst)
        return finLst

    def DFS(self, left, right, s, finLst):
        if left == 0 and right == 0:
            finLst.append(s)
        if left > 0:
            self.DFS(left - 1, right, s + '(', finLst)
        if right > left:
            self.DFS(left, right - 1, s + ')', finLst)


print(Solution().generateParenthesis(2))