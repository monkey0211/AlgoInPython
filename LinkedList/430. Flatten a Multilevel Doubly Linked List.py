"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(head)
        return head
    
    def dfs(self, node):
        if not node: return None
        if not node.child and not node.next: return node
        if not node.child:
            return self.dfs(node.next)
        
        # if node.child and node.next: need to flatten
        childnode = self.dfs(node.child)
        nextNode = node.next
        if nextNode:
            childnode.next = nextNode
            nextNode.prev = childnode
        # if no nextNode, child is the next node.
        node.next = node.child
        node.child.prev = node
        node.child = None
        return self.dfs(nextNode) if nextNode else childnode
        