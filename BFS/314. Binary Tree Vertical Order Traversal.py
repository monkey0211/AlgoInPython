# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = collections.defaultdict(list)

        queue = collections.deque([(root, 0)])

        while queue:
            node, index = queue.popleft()
            if node.left:
                queue.append((node.left, index - 1))
            if node.right:
                queue.append((node.right, index + 1))
            res[index].append(node.val)

        return [res[i] for i in sorted(res)] #sort a dict by key and return the values. 
    
