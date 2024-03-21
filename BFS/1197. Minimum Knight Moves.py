class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = collections.deque()
        queue.append((0, 0))
        step = 0
        visited = set()
        while queue:
            for q in range(len(queue)): #求最小step分层遍历记得需要for queue
                i, j = queue.popleft()   
                visited.add((i, j))
                
                if i == x and j == y:
                    return step       
                di = [1, 2, -1, -2, 1, 2, -1, -2]
                dj = [2, 1, -2, -1, -2, -1, 2, 1]
                for d in range(8):
                    newi = i + di[d]
                    newj = j + dj[d]
                    if (newi, newj) not in visited:
                        visited.add((newi, newj))
                        queue.append((newi, newj))
            step += 1 #第一步不算 step后加
        return step
        