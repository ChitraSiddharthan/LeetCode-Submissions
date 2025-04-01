class Solution(object):
    def isValidSudoku(self, board):
        for r in range(9):
            exists = set()
            for i in range(9):
                if board[r][i] == ".":
                    continue
                if board[r][i] in exists:
                    return False
                exists.add(board[r][i])
        
        for c in range(9):
            exists = set()
            for i in range(9):
                if board[i][c] == ".":
                    continue
                if board[i][c] in exists:
                    return False
                exists.add(board[i][c])
        
        for sq in range(9):
            exists = set()
            for i in range(3):
                for j in range(3):
                    r = (sq//3) * 3+i
                    c = (sq % 3) * 3+j
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in exists:
                        return False
                    exists.add(board[r][c])
        return True

        