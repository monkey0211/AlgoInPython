# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dict = collections.defaultdict(list)
        res = []
        queue = collections.deque([(root, 0)])
        minCol, maxCol = 0, 0
        while queue:
            node, index = queue.popleft()
            
            minCol = min(minCol, index)
            maxCol = max(maxCol, index)
            if node.left:
                queue.append((node.left, index - 1))
            if node.right:
                queue.append((node.right, index + 1))
            dict[index].append(node.val)

        for i in range(minCol, maxCol+1):
            res.append(dict[i])
        return res
    
