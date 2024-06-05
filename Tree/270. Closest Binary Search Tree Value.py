# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 指针从root开始遍历, 逐个比较 不断更新res, 注意diff相等的时候需要取小的值
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        if root.val == target: return target

        while root:
            if abs(root.val  - target) < abs(res - target):
                res = root.val #需要不断更新res: res is a potential result. 
            elif abs(root.val  - target) == abs(res - target):
                res = min(root.val, res)

            if target < root.val:
                root = root.left
            else:
                root = root.right
        return res
        