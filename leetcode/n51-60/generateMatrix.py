# -*- coding:utf-8 -*-
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        if n <= 0:
            return []
        res = [[]] * n
        for m in range(n):
            res[m] = [0] * n
        pathSet = set()
        i, k, direct, num = 0, 0, 0, 1
        while num <= n * n:
            now = (i, k)
            if now in pathSet or i == n or i < 0 or k == n or k < 0:
                # back one step
                if direct == 0:
                    k = k - 1
                elif direct == 1:
                    i = i - 1
                elif direct == 2:
                    k = k + 1
                else:
                    i = i + 1
                # change direction
                direct = (direct + 1) % 4
            else:
                res[i][k] = num
                pathSet.add(now)
                num = num + 1

            # get next position
            if direct == 0:
                k = k + 1
            elif direct == 1:
                i = i + 1
            elif direct == 2:
                k = k - 1
            else:
                i = i - 1

        return res


print(Solution().generateMatrix(3))