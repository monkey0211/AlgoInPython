# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

#DFS: direction的时候需要有顺序,比如clockwise,那每次dfs之后robot向右转, 
# backtrack遇到obstacle之后要goback()
# time O(mn): mxn is number of grid, space O(mn)
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        #需要先传入robot(不然需要放入dfs参数)
        self.robot = robot
        
        # direction必须要有顺序(clockwise)
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        visited.add((0, 0))
        self.dfs(0, 0, visited, 0)

    def dfs(self, x, y, visited, direction):
        self.robot.clean()

        for i in range(4):
            newDirection = (direction + i) % 4
            newx = x + self.directions[newDirection][0]
            newy = y + self.directions[newDirection][1]
            
            if (newx, newy) not in visited and self.robot.move(): #move如果是True需要走入下一格, 所以dfs之后需要goBack回退.
                visited.add((newx, newy))
                self.dfs(newx, newy, visited, newDirection)
                self.goBack() #遇到obstacle就backtrack
            self.robot.turnRight()
    
    def goBack(self):
        self.robot.turnRight()
        self.robot.turnRight()
        self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()
                
