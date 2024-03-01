# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # p, q这两个节点未必都在这棵树上出现。每个节点的值都不同
    # 用一个全局变量nodesFoundP, Q记录是否p, q都见到了
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q: return None
        self.foundP = False
        self.foundQ = False

        res = self.findLCA(root, p, q)

        if self.foundP and self.foundQ: 
            return res
        return None
    
    def findLCA(self, root, p, q):
        
        if not root: return None
   
        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)

        if root == p: self.foundP = True
        if root == q: self.foundQ = True
        
        if left and right: return root
        if root in (p, q): return root
        if left: return left
        if right: return right
        return None
