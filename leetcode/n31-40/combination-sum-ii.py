# -*- coding: utf-8 -*-


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        self.dfs(sorted(candidates), 0, target, [], res)
        return [list(x) for x in res]

    def dfs(self, candidates, start, target, tmp, res):
        if target == 0:
            res.add(tuple(tmp))
        for i in range(start, len(candidates)):
            if target >= candidates[i]:
                tmp.append(candidates[i])
                self.dfs(candidates, i + 1, target - candidates[i], tmp, res)
                tmp.pop()


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
