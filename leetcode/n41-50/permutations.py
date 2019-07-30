# -*- coding: utf-8 -*-


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def helper(index):
            if index == len(nums) - 1:
                lst = nums[:]
                res.append(lst)

            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                helper(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        helper(0)
        return res

    def permute_dfs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visit = [False] * len(nums)

        def dfs(lst):
            if len(nums) == len(lst):
                res.append(lst[:])
            else:
                for i in range(len(nums)):
                    if not visit[i]:
                        visit[i] = True
                        lst.append(nums[i])
                        dfs(lst)
                        lst.pop()
                        visit[i] = False

        dfs([])
        return res


print(Solution().permute_dfs([1, 2, 3]))
