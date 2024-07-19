# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # dfs traverse. then use list to calculate total.
        res = []
        total = 0
        self.dfs(root, res)
        for num in res:
            if low <= num <= high:
                total += num
        return total

    def dfs(self, root, res):
        if not root:
            return
        
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)


    # stack: iterative
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        range_sum =0
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                range_sum += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return range_sum