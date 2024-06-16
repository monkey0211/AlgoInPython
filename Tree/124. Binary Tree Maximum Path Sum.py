# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 类似post order 遍历. 先计算left right再计算root.val+left+right, 返回的和需要的res不是一个值
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxRes = -inf
        self.dfs(root)
        return self.maxRes
    
    def dfs(self, root):
        if not root: return 0
        # 返回给上一级的时候 要看if left or right是负的 那可以选择不用 就是用0替代 截断
        # 如果必须要从Leaf node开始 就不用max截断
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))

        res = root.val + left + right
        self.maxRes = max(res, self.maxRes)
        # 返回给上一季的只能是一边, 不会同时返回left and right(所以必须先处理左右 再处理根)
        return root.val + max(left, right) 
    
    # if and only if it is a leaf node? 
    # 不需要max截断 直接用dfs(left) or dfs(right)