#-*- coding: utf-8 -*-
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
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

lst1=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku(lst1))