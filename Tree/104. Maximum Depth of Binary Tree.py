# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    # divide conquer: max(left, right) + 1
    # time O(n) space O(logn) or O(h)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        if root.left:
            leftHeight = self.maxDepth(root.left)
        if root.right:
            rightHeight = self.maxDepth(root.right)
        
        return max(leftHeight, rightHeight) + 1
        