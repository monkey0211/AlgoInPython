class Solution:
    # BFS: try四个方向的时候用while一直走(不需要记录visited 因为可以重复经过), 停下的就是需要转弯的, 
    # 只需要把转弯的放入visited, and append to queue
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = deque()
        queue.append((start[0], start[1]))
        visited = set()
        visited.add((start[0], start[1]))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y = queue.popleft()
            if [x, y] == destination:
                return True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # while一直走
                while 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                    nx += dx
                    ny += dy
                #退回多走的一步
                nx -= dx
                ny -= dy
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return False
        