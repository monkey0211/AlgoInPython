"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
class Solution:
    # LCA3: 每个node都有parent pointer, root没有给出
    # method 1: 用set.  space O(n)
    # p的parents全部放入set, q向上找, 如果parent in set, 则是LCA
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not p or not q: return None
        parentSet = set()
        while p:
            parentSet.add(p)
            p = p.parent

        while q:
            if q in parentSet:
                return q
            else:
                q = q.parent
        return None

    # method 2: 用深度 space O(1)
    # p的parents全部放入set, q向上找, 如果parent in set, 则是LCA
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_depth = self.getDepth(p)
        q_depth = self.getDepth(q)

        #比较深度差, 更深的那个向上移动 直到same level
        for _ in range(p_depth - q_depth):
            p = p.parent
        for _ in range(q_depth - p_depth):
            q = q.parent
        
        #at the same level,return until they meet. 
        while p != q:
            p = p.parent
            q = q.parent
        return p
    
    def getDepth(self, node):
        dep = 0
        while node:
            dep += 1
            node = node.parent
        return dep