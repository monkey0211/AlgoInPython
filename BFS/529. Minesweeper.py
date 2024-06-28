class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        queue = collections.deque()
        queue.append(click)
        visited = set()
        visited.add(tuple(click))
        while queue:  
            x, y = queue.popleft()

            #计算neighbors中有多少个雷
            cnt = 0
            neighbors = self.getNeighbors(x, y, board)   
            for (newx, newy) in neighbors:
                if board[newx][newy] == "M":
                    cnt += 1
            
            #如果neighbors有雷, 把自己改成雷的个数, 停止. 如果没有, 继续把neighbors放入queue
            if cnt > 0:
                board[x][y] = str(cnt)
            else:
                board[x][y] = "B"
                for (newx, newy) in neighbors:
                    if (newx, newy) not in visited:
                        visited.add((newx, newy))
                        queue.append((newx, newy))
        return board
    
    def getNeighbors(self, x, y, board):
        res = []
        dx = [0, 1, 0, -1, 1, 1, -1, -1]
        dy = [1, 0, -1, 0, 1, -1, 1, -1]
        for i in range(8):
            newx = x + dx[i]
            newy = y + dy[i]
            if 0 <= newx < len(board) and 0 <= newy < len(board[0]):
                res.append((newx, newy))
        return res



        