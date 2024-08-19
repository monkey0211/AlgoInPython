# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # method 1: DFS in-order traverse a tree, get a node list. 
    # then link each node, and link head and tail. 
    # # time o(n) space o(n).best o(logn)树的深度
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
       
        head, prev = [None], [None]
        self.dfs(root, head, prev)
    
        prev[0].right = head[0]
        head[0].left = prev[0]
        return head[0]
    
    def dfs(self, node, head, prev):
        if not node: return
        
        self.dfs(node.left, head, prev)
        if prev[0]:    # 存在一个值比当前结点小的结点 连接node和prev[0]
            prev[0].right = node
            node.left = prev[0]
        else:         # 值比当前结点小的结点不存在:当前结点为值最小的点 记为head
            head[0] = node
        
        # prev[0]往前移动一个 作为下一个节点的左边节点
        prev[0] = node

        self.dfs(node.right, head, prev)
    
    # method 2: stack
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None

        stack = []
        res = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            res.append(node)
            if node.right:
                nextnode = node.right
                while nextnode:
                    stack.append(nextnode)
                    nextnode = nextnode.left
        
        #connect nodes within res:
        for i in range(len(res)-1):
    
            res[i].right = res[i+1]
            res[i+1].left = res[i]
        res[-1].right = res[0]
        res[0].left = res[-1]
        return res[0]


    # method 3: DFS in-order traverse a tree, get a node list. 
    # then link each node, and link head and tail. 
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
       
        res = []
        self.dfs(root, res)
        for i in range(len(res)-1):
            res[i].right = res[i+1]
            res[i+1].left = res[i]
        res[-1].right = res[0]
        res[0].left = res[-1]
        return res[0] #记得最后return头节点! not res
    
    def dfs(self, node, res):
        if not node: return
        
        self.dfs(node.left, res)
        res.append(node)
        self.dfs(node.right, res)
       