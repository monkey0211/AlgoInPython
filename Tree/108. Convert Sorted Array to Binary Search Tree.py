# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        return self.binarySearch(0, len(nums) - 1, nums)

    def binarySearch(self, left, right, nums):
        if left > right:
            return None

        # always choose right middle node as a root
        p = (left + right) // 2
        if (left + right) % 2:
            p += 1

        # preorder traversal: node -> left -> right
        root = TreeNode(nums[p])
        root.left = self.binarySearch(left, p - 1, nums)
        root.right = self.binarySearch(p + 1, right, nums)
        return root

        
        