# -*- coding: utf-8 -*-

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        pass

    def isValidSudoku(self, board):
        for arr in board:
            if not self.is_right(arr):
                return False
        
        for i in range(9):
            arr = [arr[i] for arr in board]
            if not self.is_right(arr):
                return False
        
        for k in range(0,9,3):
            for n in range(0,9,3):
                arr = [board[i][j] for i in range(k,k+3) for j in range(n,n+3)]
                if not self.is_right(arr):
                    return False

        return True
    
    def is_right(self, nums):
        lst = []
        for num in nums:
            if num in lst:
                return False
            if num !='.':
                lst.append(num)
        return True

