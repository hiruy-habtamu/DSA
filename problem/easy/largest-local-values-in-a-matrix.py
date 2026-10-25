class Solution:
    def maxNum(self,row:int,col:int,grid:list[list[int]]) ->int:
        maxInt = 0
        for i in range(row,row+3):
            for j in range(col,col+3):
                if(grid[i][j]>maxInt):
                    maxInt = grid[i][j]
        return maxInt

    
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        maxLocal = [[0 for _ in range(len(grid)-2)] for _ in range(len(grid)-2)]

        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                maxLocal[i][j] = self.maxNum(i,j,grid)
        return maxLocal