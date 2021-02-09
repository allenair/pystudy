# -*- coding:utf-8 -*-
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        resList = []
        for arr in intervals:
            if len(resList) == 0 or resList[-1][1] < arr[0]:
                resList.append(arr)
            else:
                resList[-1][1] = max(resList[-1][1], arr[1])

        return resList


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
