import collections
from math import sqrt
import math
# Check if string follows order of characters defined by a pattern or not
# ref: https://www.geeksforgeeks.org/check-if-string-follows-order-of-characters-defined-by-a-pattern-or-not-set-3/
# time o(n)
class Solution: 
    def findPath(self, matrix, desRow, desCol): 
        
        path = []
        self.desRow = desRow
        self.desCol = desCol
        self.visited = set()
        self.dfs(len(matrix) - 1, len(matrix[0]) - 1, path, matrix)
        return path

    def dfs(self, x, y, path, matrix):
        if x == self.desRow and y == self.desCol:
            return 
        
        dx = [1, 0, -1, 0, 1, 1, -1, -1]
        dy = [0, 1, 0, -1, 1, -1, 1, -1]
        for d in range(8):
            newx = dx[d] + x
            newy = dy[d] + y
            if 0 <= newx < len(matrix) and 0 <= newy < len(matrix[0]) and self.isPerfectSquare(newx, newy,matrix) and (newx, newy) not in self.visited: 
                self.visited.add((newx, newy))
                path.append((newx, newy))
                self.dfs(newx, newy, path, matrix)
                path.pop()
                self.visited.remove((newx, newy))
        
    def isPerfectSquare(self, x, y, matrix):
        value = matrix[x][y]
        if value == 1 or value == 0:
            return True
        else:
            for i in range(math.ceil(sqrt(value)) + 1):
                if i*i == value:
                    return True
        return False
matrix = [[1, 2, 1, 4, 5],
            [1, 4, 6, 7, 9]]
test = Solution()
print(test.findPath(matrix, 0, 0))
        
        
                