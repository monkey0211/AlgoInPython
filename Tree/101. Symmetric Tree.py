# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # divide conquer: 需要看两层:root相等 + 左左&右右相等 + 左右&右左相等
    # 需要加一个helper函数看下面一层 take left&right两个参数比较
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        return self.isSubSym(root.left, root.right)
    
    def isSubSym(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
        
        isOutSym = self.isSubSym(left.left, right.right)
        isInSym = self.isSubSym(left.right, right.left)
        return left.val == right.val and isOutSym and isInSym
