# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # method 1: divide conquer. 先分左右子树, 然后把左子树连到右子树去
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None

        left = self.flatten(root.left)
        right = self.flatten(root.right)

        # connect left to root.right
        if left:
            left.right = root.right
            root.right = root.left #不能是left
            root.left = None

        if right: return right
        if left: return left
        return root
    
    # method 2: iterative:stack
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        stack = [root]
        while stack:
            node = stack.pop()
    
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            # connect
            node.left = None
            if not stack:
                node.right = None
            else:
                node.right = stack[-1]
            
            