class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        building = 0
        dist = [[0]*len(grid[0]) for i in range(len(grid))]
        count = [[0]*len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    building += 1
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, count, dist) #不断更新count and dist并return
        minDist = inf
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and count[i][j] == building:
                    minDist = min(minDist, dist[i][j])
        return minDist if minDist != inf else -1
    
    def bfs(self, grid, x, y, count, dist):
        queue = collections.deque()
        queue.append((x, y))

        visited = set()
        step = 0
        while queue:
            step += 1
            for q in range(len(queue)):
                i, j = queue.popleft()
                visited.add((i, j))

                di = [0, 1, 0, -1]
                dj = [1, 0, -1, 0]
                for d in range(4):
                    newi = i + di[d]
                    newj = j + dj[d]
                    if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and (newi, newj) not in visited and grid[newi][newj] == 0:
                        queue.append((newi, newj))
                        visited.add((newi, newj))
                        dist[newi][newj] += step
                        count[newi][newj] += 1
