# -*- coding: utf-8 -*-


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        for i in range(n // 2 + 1):
            for j in range(i, n-i):
                matrix[i][j], matrix[j][n - i], matrix[n - i][n - j], matrix[n - j][i] = matrix[n - j][i], matrix[i][j], matrix[j][n - i], matrix[n - i][n - j]

        return matrix


print(Solution().rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11,12],[13,14,15,16]]))
