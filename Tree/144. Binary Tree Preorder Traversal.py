from typing import List
from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # method 1: traverse
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if not root:
            return
        self.res.append(root.val)    
        self.traverse(root.left)
        self.traverse(root.right)

# method2: interative(stack)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return [] #must have. 否则root.val invalid
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
