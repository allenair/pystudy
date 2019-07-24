#-*- coding: utf-8 -*-
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], res)
        return res

    def dfs(self, candidates, start, target, tmp, res):
        if target == 0:
            res.append(tmp[:])

        for i in range(start, len(candidates)):
            if target >= candidates[i]:
                tmp.append(candidates[i])
                self.dfs(candidates, i, target - candidates[i], tmp, res)
                tmp.pop()


print(Solution().combinationSum([2, 3, 5], 8))
