# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # method 1: interative: in-order traversal + compare curNode & stack[-1]
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        stack = []
        while root:
            stack.append(root)
            root = root.left
        
        lastNode = stack[-1]
        while stack:
            node = stack.pop()
            if node.right:
                nextnode = node.right
                while nextnode:
                    stack.append(nextnode)
                    nextnode = nextnode.left
            
            #the only difference compared to in-order: compare the curNode and previous node in stack
            if stack:
                if stack[-1].val < lastNode.val: #must look at False, all else are True
                    return False
                lastNode = stack[-1] #do it everytime: outside of "If"
        return True
   
   # method 2: DFS + check final result list.  
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        self.res = []
        self.dfs(root)
        for i in range(1, len(self.res)):
            if self.res[i] <= self.res[i - 1]:
                return False
        return True

    def dfs(self, root):
        if not root: return 

        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)
