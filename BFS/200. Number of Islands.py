class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        visited = set()
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]== "1" and (i, j) not in visited:
                    visited.add((i, j))
                    self.bfs(grid, i, j, visited) #bfs within for loop. 
                    cnt += 1
        return cnt

    def bfs(self, grid, x, y, visited):
        queue = collections.deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            for i in range(4):
                newx = x + dx[i]
                newy = y + dy[i]
                if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and grid[newx][newy] == "1" and (newx, newy) not in visited:
                    queue.append((newx, newy))
                    visited.add((newx, newy))
 
 # method 2: DFS  
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        visited =set()
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]== "1" and (i, j) not in visited:
                    visited.add((i, j))
                    self.dfs(grid, i, j, visited)
                    cnt += 1
        return cnt

    def dfs(self, grid, x, y, visited):
        if x < 0 or x >=len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != "1":
            return    
        #也可以visited过的元素变成0  grid[x][y] = "0" 
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and grid[newx][newy] == "1" and (newx, newy) not in visited:
                visited.add((newx, newy))
                self.dfs(grid, newx, newy, visited)
                        
                
