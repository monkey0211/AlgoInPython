'''
variation of LC489:https://leetcode.com/problems/robot-room-cleaner/description/
find cheese and instead of manual rotation, the robot can move in any direction
assume cheese 
'''
from typing import List

class Robot:
    def check_cheese(self) -> bool:
        pass 
    
    # 指的是facing的下一个grid是否可行: T/F(如果T不需要走进去 只需要判断)
    def move(self) -> bool: 
        pass

def find_cheese(robot: Robot):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] 
    visited = set()
    visited.add((0, 0))
    dfs(robot, directions, 0, 0, visited)

def dfs(robot: Robot, directions: List[tuple[int, int]], x: int, y: int, visited: set) -> List[int]:
    if robot.check_cheese():
        return [x, y] # return the target grid.
    
    for i in range(4):
        nx = x + directions[i][0]
        ny = y + directions[i][1]
        if (nx, ny) not in visited and robot.move():
            visited.add(nx, ny)
            dfs(robot, directions, nx, ny, visited)