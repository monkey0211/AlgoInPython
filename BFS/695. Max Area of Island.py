class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    area = self.bfs(grid, i, j, visited)
                    maxArea = max(maxArea, area)
        return maxArea
    
    def bfs(self, grid, x, y, visited):
        queue = collections.deque()
        queue.append((x, y))
        area = 0
        while queue:
            x, y = queue.popleft()
            area += 1
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            for d in range(4):
                newx = x + dx[d]
                newy = y + dy[d]
                if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and (newx, newy) not in visited and grid[newx][newy] == 1:
                    visited.add((newx, newy))
                    queue.append((newx, newy))
        return area