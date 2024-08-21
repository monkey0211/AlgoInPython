'''

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#  先in order traversal 把所有的点存到array里, 
# 再用inorder sorted array build BST(同LC94+LC108)

# time O(n) space O(n)
    def balanceBST(self, root: TreeNode) -> TreeNode:

        nums = []
        self.inorder(root, nums)

        newroot = self.build(0, len(nums) - 1, nums)
        return newroot

    def inorder(self, root, nums):
        if not root:return None

        root.left = self.inorder(root.left, nums)
        nums.append(root.val)
        root.right = self.inorder(root.right, nums)

    def build(self, l, r, nums):
        if l > r:
            return None

        mid = l + (r - l) // 2
        root = TreeNode(nums[mid])
        root.left = self.build(l, mid - 1, nums)
        root.right = self.build(mid + 1, r, nums)

        return root