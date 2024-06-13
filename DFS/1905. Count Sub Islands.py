class Solution:
    # dfs:先remove all invalid subisland: grid2[i][j]==0 and grid1[i][j]==1的都变为0
    # 2. count #of island in grid2.
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid1 or not grid2: return 0

        # 1. remove all invalid subisland: grid2[i][j]==0 and grid1[i][j]==1的都变为0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    self.dfs(i, j, grid2)
        # 2. count #of island in grid2.
        cnt = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1:
                    cnt += 1
                    self.dfs(i, j, grid2)
        return cnt
    def dfs(self, x, y, grid):

        grid[x][y] = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and grid[newx][newy] == 1:
                self.dfs(newx, newy, grid)


                    