class Solution:
    #dp: dp[i][j]: the minimum sum to get to dp[i][j]
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        dp = grid

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]   
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]
       
        