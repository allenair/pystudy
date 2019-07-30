# -*- coding: utf-8 -*-


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        new_nums = sorted(nums)
        visit = [False] * len(nums)

        def dfs(lst):
            if len(lst) == len(new_nums):
                res.append(lst[:])
            else:
                for i in range(len(new_nums)):
                    if visit[i]:
                        continue
                    if i > 0 and new_nums[i] == new_nums[i - 1] and not visit[i - 1]:
                        continue

                    visit[i] = True
                    lst.append(new_nums[i])
                    dfs(lst)
                    lst.pop()
                    visit[i] = False

        dfs([])
        return res


print(Solution().permuteUnique([1, 2, 1]))
