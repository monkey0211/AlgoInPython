# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS: 每一层append一个[], dfs return当前层的node, 
# 如果是Leaf: res[-1].append(node.val),但是dfs自己return None(cutoff)
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        while root:
            res.append([])
            root = self.dfs(root, res)
        return res
    
    def dfs(self, node, res):
        if not node:
            return None
        
        if not node.left and not node.right: #leaf node
            res[-1].append(node.val)
            return None # append to result但是不return node(cutoff)
        
        node.left = self.dfs(node.left, res)
        node.right = self.dfs(node.right, res)
        return node #其他情况都return node

        