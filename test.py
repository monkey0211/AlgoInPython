from math import sqrt
from typing import List
import heapq

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def rangeBST(self, root, low, high):
        if not root: return 0
  
        if root.val < low:
            return self.rangeBST(root.right, low, high)
        if root.val > high:
            return self.rangeBST(root.left, low, high)
        return root.val + self.rangeBST(root.left, low, high) + self.rangeBST(root.right, low, high)
    

root = TreeNode(4)
left = TreeNode(1)
right = TreeNode(8)
root.left = left
root.right = right
test = Solution()
print(test.rangeBST(root, 3, 9))