class Solution:
    # BFS time O(mn*mn) space O(mn)
    # 1. 从每个1(building)开始bfs, 记录dist and count(该点经过了多少个building)
    # 2. 从每个0开始, if count==building个数, 更新minDist
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        building = 0
        #dist记录(i, j)到每个building“1”的距离加和, 所以最后是k个building的距离和
        #count记录(i,j)可以经过多少个building
        dist = [[0]*len(grid[0]) for i in range(len(grid))]
        count = [[0]*len(grid[0]) for i in range(len(grid))]
        
        # 对每一个building, #bfs更新dist and count, 并计算building个数
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, count, dist) 
                    building += 1
        
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

        


    # method 2: 节省space版本: bfs without visited.
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist, cnt = collections.defaultdict(int), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, m, n, i, j, cnt, dist)
                    cnt += 1 #cnt 表示找到了几个building
                    
        min_dist = float("inf")
        for (x, y), step in dist.items():
            if grid[x][y] == -cnt:
                min_dist = min(min_dist, step)
        return min_dist if min_dist != float("inf") else -1

    def bfs(self, grid, m, n, i, j, cnt, dist):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = collections.deque([(0, i, j)]) # step, x, y
        while queue:
            step, x, y = queue.popleft()
            step += 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == -cnt:
                    queue.append((step, nx, ny))
                    grid[nx][ny] -= 1  #每走一步就把grid从0改到-1 -cnt就是找到的building个数
                    dist[(nx, ny)] += step   