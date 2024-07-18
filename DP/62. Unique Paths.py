class Solution:
    # method 1: dp
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for i in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    # method 2: dfs + memo
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a memoization table to store computed results
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        
        # Call the recursive function to compute unique paths
        return self.dfs(0, 0, m, n, memo)
    
    def dfs(self, x: int, y: int, m: int, n: int, memo: List[List[int]]) -> int:
        # If we reach the destination (bottom-right corner), return 1
        if x == m - 1 and y == n - 1:
            return 1
        
        # If we have already computed the result for this cell, return it from the memo table
        if memo[x][y] != -1:
            return memo[x][y]
        
        # Calculate the number of unique paths by moving right and down
        rightPaths = 0
        downPaths = 0
        
        # Check if it's valid to move right
        if x < m - 1:
            rightPaths = self.dfs(x + 1, y, m, n, memo)
        
        # Check if it's valid to move down
        if y < n - 1:
            downPaths = self.dfs(x, y + 1, m, n, memo)
        
        # Store the result in the memo table and return it
        memo[x][y] = rightPaths + downPaths
        return memo[x][y]
    
        return len(res)
    
    # 如果要求只返回任意一条path
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(x, y, path):
            # If the robot reaches the bottom-right corner
            if x == m - 1 and y == n - 1:
                if not paths: #之前没找到过
                    paths.append(path + [(x, y)])
                return
            
            # If this position has been computed before, use the memoized paths
            if (x, y) in memo:
                return
        
            
            # Move right if possible
            if y + 1 < n:
                dfs(x, y + 1, path + [(x, y)])
            
            # Move down if possible
            if x + 1 < m:
                dfs(x + 1, y, path + [(x, y)])
            
            # Store the current paths in memo
            memo.add((x,y))
        
        paths = []
        memo = set()
        dfs(0, 0, [])
        return len(paths)