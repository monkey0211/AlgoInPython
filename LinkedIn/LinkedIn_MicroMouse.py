# the mouse needs to search and discover the maze. the mouse can move one step at a time and returned to any previous visited location 
# if needed. 

class Solution:
    def __init__(self, mouse: Mouse):
        self.mouse = mouse
        self.visited = set()
        
    def moveMouse(self, goal):
        return self.helper(goal, self.mouse.getCurrentLoation())
    
    def helper(self, goal, current):
        if current == goal:
            return True
        self.visited.add(self.mouse.getCurrentLocation())