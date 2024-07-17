class Solution:
# 只有两个island 找到shortest bridge连接两个岛
#1. Find the firstland的初始点 -> firstCell = (i, j)
#DFS - Use firstCell to explore Island A and store all land cells in a queue
#BFS - Find the shortest path from Island A cells -> Island B. Only storing water or unvisited cells in our queue
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # 1. Find first cell in island A
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    firstCell = (i, j)
                    break

  
        # 2. DFS: find and Load all land cells in island A
        queue = collections.deque()
        self.dfs(firstCell[0], firstCell[1],queue, grid)

        # 3. BFS: find shortest path from island A cells -> island B
        while queue:
            x, y, dist = queue.popleft()
            for newx, newy in self.findValidNeighbors(x, y, grid):
                
                # Found Island B
                if grid[newx][newy] == 1:
                    return dist
                # Found Water
                elif grid[newx][newy] == 0:
                    queue.append((newx, newy, dist + 1))
                    grid[newx][newy] = -1 # mark as seen
        return -1

    def dfs(self, i, j, queue, grid):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            queue.append((i, j, 0)) # Load Island A to queue
            grid[i][j] = -1       # mark as seen

            for newx, newy in self.findValidNeighbors(i, j, grid):
                self.dfs(newx, newy, queue, grid)
        

    def findValidNeighbors(self, x, y, grid):
        res = []
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for d in range(4):
            newx = x + dx[d]
            newy = y + dy[d]
            if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]):
                res.append((newx, newy))
        return res