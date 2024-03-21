class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        minute = 0
        count = 0
        queue = collections.deque()
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    count += 1
        if count == 0: return 0

        while queue:
            minute += 1
            for i in range(len(queue)):
                x, y = queue.popleft()
                visited.add((x, y))
                dx = [0, 1, 0, -1]
                dy = [1, 0, -1, 0]
                for i in range(4):
                    newx = x + dx[i]
                    newy = y + dy[i]
                    if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and (newx, newy) not in visited and grid[newx][newy] == 1:
                        visited.add((newx, newy)) # if save space, can change grid[i][j] = 2
                        queue.append((newx, newy))
                        count -= 1
                        if count == 0: 
                            return minute      
            
        return -1
        
        