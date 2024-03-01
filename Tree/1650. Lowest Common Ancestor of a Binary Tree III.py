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
        