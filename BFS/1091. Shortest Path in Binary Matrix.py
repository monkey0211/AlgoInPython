class Solution:
    # standard BFS + visited(if only read allowed), visited can change to: grid[newx][newy] = 1 after visited(save space)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] != 0 or grid[-1][-1] != 0: return -1
        step = 0
        queue = collections.deque()
        queue.append((0, 0))

        while queue:
            step += 1 #step = 2
            grid[0][0] = 1
            for i in range(len(queue)):
                x, y = queue.popleft()      
                if x == len(grid)-1 and y == len(grid[0])-1: #此处已经排除grid[x][y] = 1的情况 所以不需要加(如果加了就不对了, 因为grid[newx][newy]已经被改了值)
                    return step
                
                dx = [0, 1, 0, -1, 1, 1, -1, -1]
                dy = [1, 0, -1, 0, 1, -1, 1, -1]
                for d in range(8):
                    newx = x + dx[d]
                    newy = y + dy[d]
                    if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and grid[newx][newy] == 0:
                        queue.append((newx, newy)) 
                        grid[newx][newy] = 1
        return -1 #此处要return -1, not step
