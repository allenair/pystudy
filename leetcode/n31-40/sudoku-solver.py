# -*- coding: utf-8 -*-


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [[0] * 10 for i in range(9)]
        col = [[0] * 10 for i in range(9)]
        box = [[0] * 10 for i in range(9)]

        for i in range(9):
            for k in range(9):
                if board[i][k] != '.':
                    num = int(board[i][k])
                    row[i][num] = 1
                    col[k][num] = 1
                    box[i // 3 * 3 + k // 3][num] = 1

        self.solve(board, 0, 0, row, col, box)

    def solve(self, board, x, y, row, col, box):
        if x==9:
            return True
        
        ny = (y+1) % 9
        nx = x+1 if ny==0 else x

        if board[x][y]!='.':
            return self.solve(board, nx, ny, row, col, box)

        box_index = x//3*3+y//3
        for i in range(1,10):
            if (not row[x][i]) and (not col[y][i]) and (not box[box_index][i]):
                board[x][y]=str(i)
                row[x][i]=1
                col[y][i]=1
                box[box_index][i]=1
                if self.solve(board, nx, ny, row, col, box):
                    return True
                board[x][y]='.'
                row[x][i]=0
                col[y][i]=0
                box[box_index][i]=0
        
        return False

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
print(board)

   
