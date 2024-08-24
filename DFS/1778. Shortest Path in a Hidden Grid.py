# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        

# 此题没有grid和target 所以需要先dfs找到所有grid坐标(visited的即可), target cell
# 然后再bfs在这里找最短.(此时因为是在visited里面找, 每找到一个反向remove即可)
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        reverse_directions = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        visited = set() #记录走过的所有grid
        target = []
        self.dfs(0, 0, target, visited, directions, reverse_directions, master)

        if not target:
            return -1

        queue = collections.deque([(0, 0, 0)])
        visited.remove((0, 0))
        endpoint = target[0]
        
        while queue:
            x, y, steps = queue.popleft()
            if (x, y) == endpoint:
                return steps

            for d in directions:
                new_x, new_y = directions[d][0] + x, directions[d][1] + y
                if (new_x, new_y) not in visited:
                    continue
                visited.remove((new_x, new_y))
                queue.append((new_x, new_y, steps + 1))
        return -1

    def dfs(self, x: int, y: int, target: List[int], visited: set[tuple[int, int]], directions: dict[str, tuple[int, int]], reverse_directions: dict[str, str], master: 'GridMaster'):
        if master.isTarget():
            target.append((x, y)) #这里找到target不能return, 因为还需要找到其他所有grid.
            
            #如果需要找任意一个路线(不是最短路):
            # path = tmp[:]
            # return 
            # for 后面需要:
            # tmp.append((new_x, new_y))
            # dfs()
            # tmp.pop()
    
        for d in directions:
            new_x, new_y = directions[d][0] + x, directions[d][1] + y
            if (new_x, new_y) not in visited and master.canMove(d):
                visited.add((new_x, new_y))
                master.move(d) # move到下一个
                self.dfs(new_x, new_y, target, visited, directions, reverse_directions, master)
                master.move(reverse_directions[d]) # return back
    
