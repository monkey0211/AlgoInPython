# Definition for a binary tree node.
from typing import Optional
import collections 


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # method 1: DFS preorder traversal (node节点可以是multi-digit情况)
    def sumNumbers1(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = []
        tmp = "" # the path from root to leaf
        self.dfs(root, res, tmp) 
        return sum(res)

    def dfs(self, node: TreeNode, res: list, tmp: str):
    
        if node.left == None and node.right == None:
            tmp += str(node.val)
            res.append(int(tmp))
            return
        tmp += str(node.val)
        if node.left:
            self.dfs(node.left, res, tmp)  
        if node.right:
            self.dfs(node.right, res, tmp)
    
    # method 2: BFS queue (只适用于node上是single digit情况)
    def sumNumbers2(self, root: Optional[TreeNode]) -> int:
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

root = TreeNode(10)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right
test = Solution()
print(test.sumNumbers1(root))
print(test.sumNumbers2(root))