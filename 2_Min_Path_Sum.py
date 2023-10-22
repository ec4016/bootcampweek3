class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        #base case
        for i in range(1,n):
            grid[0][i] += grid[0][i-1]
        
        for j in range(1,m):
            grid[j][0] += grid[j-1][0]
        
        #in place dp
        for j in range(1, m):
            for i in range(1,n):
                grid[j][i] += min(grid[j-1][i], grid[j][i-1])

        return grid[-1][-1]
