class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # keeping track of a group id (or index), that is unique for each group. 
        # Then, we'll only add areas of neighboring groups with different ids
        if not grid: return 0
        area = {} #area[groupId] = area, groupId is the 
        res = 0
        groupId = 2
        size = [0]
        # dfs to calculate current area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size = self.dfs(i, j, grid, groupId) # why this "pass by value" works?
                    area[groupId]  = size #把所有走过的grid[i][j]都变成相应的index, 此时就不需要visited了(因为已经改了index)
                    res = max(res, area[groupId])
                    groupId += 1
      
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxArea = 1 # 不能在if里面初始化, 不然local variable看不到
                visited = set() #此处visited需要放的是groupID
                if grid[i][j] == 0: #遍历所有的0, 尝试变成1之后计算连起来的area
                    
                    for (newi, newj) in self.getNeighbors(i, j):
                        if self.isValid(newi, newj, grid) and grid[newi][newj] not in visited and grid[newi][newj] in area:
                            visited.add(grid[newi][newj])
                            newGroupId = grid[newi][newj]
                            maxArea += area[newGroupId]
                    res = max(res, maxArea) # 注意res位置 是需要对每一个0更新面积
        return res

    def dfs(self, x, y, grid, groupId):
        count = 1
        grid[x][y] = groupId # why here?

        for (newx, newy) in self.getNeighbors(x, y):
            if self.isValid(newx, newy, grid) and grid[newx][newy] == 1:
                grid[newx][newy] = groupId
                count += self.dfs(newx, newy, grid, groupId)
        return count
    
    def getNeighbors(self, x, y):
        res = []
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for d in range(4):
            newx = x + dx[d]
            newy = y + dy[d]
            res.append((newx, newy))
        return res
    
    def isValid(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])



        