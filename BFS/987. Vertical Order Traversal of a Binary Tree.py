# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 最后结果输出需要按左->右, 上->下排序 
    # O(k * N/KlogN/k) + O(N) = O(NlogN/k), k is the number of columns and O(N) for tree traversal
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dict = collections.defaultdict(list) # dict[col] = (row, value)
        queue = collections.deque([(root, 0, 0)])
        minj, maxj = 0, 0

        while queue:
            node, i, j = queue.popleft()
            minj = min(j, minj)
            maxj = max(j, maxj)
            if node.left:
                queue.append((node.left, i + 1, j - 1))
            if node.right:
                queue.append((node.right, i + 1, j + 1))
            dict[j].append((i, node.val))
        
        res = []
        for col in range(minj, maxj + 1):
            res.append([val for row, val in sorted(dict[col])])
        return res