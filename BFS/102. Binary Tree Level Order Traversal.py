# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []

        queue = collections.deque([root]) #queue里装的是node, res是value
        while queue:
            temp = []
            for i in range(len(queue)):    
                root = queue.popleft()
                temp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(temp)
        return res

            
        