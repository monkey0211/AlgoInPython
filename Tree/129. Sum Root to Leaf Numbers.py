# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # method 1: DFS preorder traversal
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = []
        tmp = ""
        self.dfs(root, res, tmp)
        print(res)
        return sum(res)

    def dfs(self, node: TreeNode, res: list, tmp: str):
        # if not node:
        #     return
        if node.left == None and node.right == None:
            tmp += str(node.val)
            res.append(int(tmp))
            return
        tmp += str(node.val)
        if node.left:
            self.dfs(node.left, res, tmp)  
        if node.right:
            self.dfs(node.right, res, tmp)
    
    # method 2: BFS queue
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        total = 0
        queue = collections.deque()
        queue.append((root, root.val))

        while queue:
            node, pathSum = queue.popleft()

            if not node.left and not node.right:
                total += pathSum
            if node.left:
                queue.append((node.left, pathSum*10 + node.left.val))
            if node.right:
                queue.append((node.right, pathSum*10 + node.right.val))
        return total