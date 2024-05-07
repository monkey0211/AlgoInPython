class Solution:
    # standard BFS + visited(if only read allowed), visited can change to: grid[newx][newy] = 1 after visited(save space)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] != 0: return -1
        step = 0
        visited = set()
        visited.add((0, 0))
        queue = collections.deque()
        queue.append((0, 0))

        while queue:
            step += 1
            for q in range(len(queue)):
                x, y = queue.popleft()
                print(x, y, step)
                if grid[x][y] == 0 and x == len(grid)-1 and y == len(grid[0])-1:
                    return step
                
                dx = [0, 1, 0, -1, 1, 1, -1, -1]
                dy = [1, 0, -1, 0, -1, 1, 1, -1]
                for i in range(8):
                    newx = x + dx[i]
                    newy = y + dy[i]
                    if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and (newx, newy) not in visited and grid[newx][newy] == 0:
                        visited.add((newx, newy))
                        queue.append((newx, newy))
        return -1
        