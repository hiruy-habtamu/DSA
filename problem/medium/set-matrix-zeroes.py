class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        cols = []
        rows = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]==0):
                    rows.append(i)
                    cols.append(j)

        for r in rows:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0
        for c in cols:
            for i in range(len(matrix)):
                matrix[i][c] = 0