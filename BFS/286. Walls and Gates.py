class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = collections.deque()
        if not rooms: return 
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j)) 
        while queue:
            x, y = queue.popleft()
            
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            for i in range(4):
                newx = x + dx[i]
                newy = y + dy[i]
                if 0 <= newx < len(rooms) and 0 <= newy < len(rooms[0]) and rooms[newx][newy]>rooms[x][y] + 1:
                    rooms[newx][newy] = rooms[x][y] + 1
                    queue.append((newx, newy))
