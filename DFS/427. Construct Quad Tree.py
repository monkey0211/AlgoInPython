"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
# https://www.youtube.com/watch?v=UQ-1sBMV0v4

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.dfs(len(grid), 0, 0, grid)
    
    def dfs(self, n, r, c, grid):
        # base case: 如果quad里面的所有元素都相同, 就不需要继续breakup, 可以直接return
        allSame = True
        for i in range(n):
            for j in range(n):
                if grid[r][c] != grid[r+i][c+j]:
                    allSame = False
                    break
        if allSame:
            return Node(grid[r][c], True) #leafNode的定义. 
        
        n = n // 2 #split拆分
        topleft = self.dfs(n, r, c, grid)
        topright = self.dfs(n, r, c + n, grid)
        bottomleft = self.dfs(n, r + n, c, grid)
        bottomright = self.dfs(n, r + n, c + n, grid)
        
        #create the current node(value不重要 任何一个都可以), 参数顺序要和Node定义的参数顺序一致
        return Node(0, False, topleft, topright, bottomleft, bottomright) 

        

        