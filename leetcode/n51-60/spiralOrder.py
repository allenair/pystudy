# -*- coding:utf-8 -*-
class Solution:
    def spiralOrder(self, matrix: [[]]) -> []:
        if matrix == None or len(matrix) == 0:
            return []
        res = []
        pathSet = set()
        m, n = len(matrix), len(matrix[0])
        i, k, direct = 0, 0, 0
        num = m * n
        while len(pathSet) < num:
            now = (i, k)
            if now in pathSet or i == m or i < 0 or k == n or k < 0:
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
                res.append(matrix[i][k])
                pathSet.add(now)

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


print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
