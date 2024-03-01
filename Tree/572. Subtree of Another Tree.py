# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #先判断是不是same tree,如果不是 比较(s.left, t) 和 (s.right, t)是不是same tree
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False

        # 此处left right都是isSubtree 不能只是sameTree(因为可能是sub-sub tree)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return self.isSameTree(root, subRoot) or left or right

    def isSameTree(self, root, subRoot):
        if not root and not subRoot: return True
        if not root or not subRoot: return False

        return root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right) 
