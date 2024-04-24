"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    # DFS in-order traverse a tree, get a node list. link each node, and link head and tail. ->need extra space O(n)
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None

        nodes = []
        self.dfs(root, nodes)

        for i in range(len(nodes)-1):
            nodes[i].right = nodes[i+1]
            nodes[i+1].left = nodes[i]

        nodes[-1].right = nodes[0]
        nodes[0].left = nodes[-1]
        return nodes[0]

    def dfs(self, node, nodes):
        if not node: return 

        self.dfs(node.left, nodes)
        nodes.append(node)
        self.dfs(node.right, nodes)
