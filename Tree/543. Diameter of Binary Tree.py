# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 无脑left, right, 需要一个辅助函数记录每次的height并不断更新(global variable)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        self.res = 0
        self.maxHeight(root)
        return self.res

    def maxHeight(self, root):
        
        if not root: return 0
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)
        #3. 最后写这个逻辑: 每次比较前一个res和新的left+right结果
        self.res = max(self.res, left + right)

        # 2. return的是左右Max + 1, 和above不一样
        return max(left, right) + 1
        