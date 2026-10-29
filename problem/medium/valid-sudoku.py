class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        r = len(board)
        c = len(board)
        count = []
        for i in range(r):
            for j in range(c):
                number = board[i][j]
                if(number!="."):
                    count+=[
                    (i,number),
                    (number,j),
                    (i//3,j//3,number)]
        return len(count) == len(set(count))