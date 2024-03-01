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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if not root:
            return
               
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)
        
    # method 2: interative. stack
    # 先找到deep left node, until left tree is all done.  
    # find first right node, repeat finding deep left node.
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        res = []
        stack = []
        #1.确定起点: leftmost node
        while root:
            stack.append(root)
            root = root.left
        
        #2.pop element from stack and append to res. then check right node.
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                nextnode = node.right
                while nextnode:
                    stack.append(nextnode)
                    nextnode = nextnode.left
        return res


        