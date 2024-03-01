# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
      # divide conquer: 1)both children are BBT 2) height <= 1
        # 需要定义一个helper函数 两个返回值: isBalanced, height
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        isBalanced, height = self.validate(root)
        return isBalanced

    def validate(self, root):
        if not root:
            return True, 0

        if not root.left and not root.right:
            return True, 1

        isLeftBalanced, leftHeight = self.validate(root.left)
        isRightBalanced, rightHeight = self.validate(root.right)

        rootHeight = max(leftHeight, rightHeight) + 1
        if isLeftBalanced == True and isRightBalanced == True and abs(leftHeight - rightHeight) <= 1:
            return True, rootHeight
        else:
            return False, rootHeight
    