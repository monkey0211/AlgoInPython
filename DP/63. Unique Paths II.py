'''
首先,我们检查输入是否有效,以及起点是否被障碍物阻挡。如果是,直接返回0。
我们创建一个和输入网格大小相同的dp表。dp[i][j]表示从起点到(i,j)位置的不同路径数。
初始化起点dp[0][0] = 1。
初始化第一行和第一列。如果没有障碍物,当前格子的路径数等于左边或上边格子的路径数；如果有障碍物,路径数为0。

填充dp表的其余部分。对于每个格子:
如果没有障碍物,路径数等于上面格子和左边格子的路径数之和。
如果有障碍物,路径数为0。
最后,返回dp[m-1][n-1],即终点的路径数。
这个解决方案的时间复杂度是O(mn),空间复杂度也是O(mn),其中m和n分别是网格的行数和列数。
'''
from typing import List, Tuple

def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0
    
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the starting point
    dp[0][0] = 1
    
    # Initialize first row
    for j in range(1, n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = dp[0][j-1]
        else:
            dp[0][j] = 0
    
    # Initialize first column
    for i in range(1, m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][0] = 0
    
    # Fill the dp table
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = 0
    
    return dp[m-1][n-1]

'''
空间优化版本 i那一维可以省略掉 只用更新j的维度
等于是复用一行的空间
时间复杂度O(mn) 空间复杂度O(n), 其中m和n分别是网格的行数和列数。
'''
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0
    
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * n
    
    # Initialize the first element
    dp[0] = 1
    
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j-1]
    
    return dp[n-1]

'''
变种: 要求返回任意一条path
我们使用一个布尔型的 dp 表，其中 dp[i][j] 表示是否存在一条从起点到 (i,j) 的路径。
我们首先填充 dp 表，方法类似于之前的问题：
如果当前格子不是障碍物，且可以从上方或左方到达，则标记为 True。
否则标记为 False。
填充完 dp 表后，我们检查终点 dp[m-1][n-1] 是否可达。如果不可达，返回空列表。
如果终点可达，我们从终点开始回溯找到一条路径：
从终点开始，每次检查是否可以向上移动或向左移动。
选择其中一个可行的方向，并将该点加入路径。
重复这个过程直到到达起点。
最后，我们将路径反转，使其从起点开始到终点结束。
这个解决方案的时间复杂度是 O(mn)，空间复杂度也是 O(mn)，其中 m 和 n 分别是网格的行数和列数。
'''
def find_path(obstacle_grid: List[List[int]]) -> List[Tuple[int, int]]:
    if not obstacle_grid or obstacle_grid[0][0] == 1:
        return []
    
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    dp = [[False] * n for _ in range(m)]
    
    # Initialize the starting point
    dp[0][0] = True
    
    # Fill the first row
    for j in range(1, n):
        if obstacle_grid[0][j] == 0 and dp[0][j-1]:
            dp[0][j] = True
    
    # Fill the first column
    for i in range(1, m):
        if obstacle_grid[i][0] == 0 and dp[i-1][0]:
            dp[i][0] = True
    
    # Fill the dp table
    for i in range(1, m):
        for j in range(1, n):
            if obstacle_grid[i][j] == 0 and (dp[i-1][j] or dp[i][j-1]):
                dp[i][j] = True
    
    # If there's no path to the end, return an empty list
    if not dp[m-1][n-1]:
        return []
    
    return backtrack_path(dp)

def backtrack_path(dp: List[List[bool]]) -> List[Tuple[int, int]]:
    m, n = len(dp), len(dp[0])
    path = [(m-1, n-1)]
    i, j = m-1, n-1
    while i > 0 or j > 0:
        if i > 0 and dp[i-1][j]:
            i -= 1
        elif j > 0 and dp[i][j-1]:
            j -= 1
        path.append((i, j))
    
    return path[::-1]  # Reverse the path to get start to end

# Test the solution
# Example 1
obstacle_grid1 = [[0,0,0],[0,1,0],[0,0,0]]
print(f"Example 1 Output: {find_path(obstacle_grid1)}")

# Example 2
obstacle_grid2 = [[0,1],[0,0]]
print(f"Example 2 Output: {find_path(obstacle_grid2)}")

