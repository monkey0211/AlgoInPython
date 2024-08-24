# the mouse needs to search and discover the maze. the mouse can move one step at a time and returned to any previous visited location 
# if needed. 

class Mouse:
    def __init__(self) -> None:
        pass
    
    # def canMove(self, direction: str) -> bool:
    def getCurrentWallStatus(self, direction: str) -> bool:
        pass
    
    def move(self, direction: str) -> bool:
        pass
    
    def getCurrentLocation(self):
        pass
        
class Location:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

class Solution:
    def __init__(self, mouse: Mouse):
        self.mouse = mouse
        self.visited = set()
        self.res = []
        self.directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.reverse_directions = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        
    def moveMouse(self, target: Location):
        self.res = []
        self.dfs(0, 0, target)
        
        if not self.res:
            return -1

        # BFS找最短路
        queue = deque([(0, 0, 0)])
        self.visited.remove((0, 0))
        endpoint = target[0]
        
        while queue:
            currLocation, steps = queue.popleft()
            if currLocation == target:
                return steps

            for d in self.directions:
                newx, newy = self.directions[d][0] + currLocation.x, self.directions[d][1] + currLocation.y
                newLocation = Location(newx, newy)
                if newLocation not in self.visited:
                    continue
                self.visited.remove(newLocation)
                queue.append((newLocation, steps + 1))
        return -1     
    
    def dfs(self, curLocation: Location, target: Location):
        if curLocation == target:
            self.res.append(curLocation)
            
        for d in self.directions:
            newx, newy = self.directions[d][0] + curLocation.x, self.directions[d][1] + curLocation.y
            nextLocation = Location(newx, newy)
            if nextLocation not in self.visited and self.mouse.getCurrentWallStatus(d):
                self.visited.add(nextLocation)
                self.mouse.move(d)
                self.dfs(nextLocation)
                self.mouse.move(self.reverse_directions[d])
            
   
            
            
        
    