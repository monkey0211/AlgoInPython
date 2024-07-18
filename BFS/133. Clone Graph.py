"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    # 1. 得到所有的点bfs. visited表示
    # 2. 用map存old A->A'的对应关系 
    # 3. 得到所有的new A' 的neighbors(对应关系)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        #1. BFS traverse from root to get all graph nodes(通过一个点去找到所有的图上的点)
        queue = collections.deque([node])
        
        visited = set()
        while queue:
            n = queue.popleft()
            visited.add(n)
            for nei in n.neighbors:
                if nei not in visited:
                    queue.append(nei)
                    visited.add(nei)
        
        #2. for every visited, copy all nodes, store in old->new mapping. 
        mapping = {} #用来存 A-> A'
        for n in visited:
            mapping[n] = Node(n.val)
            
        #3. for every visited, copy all neighbors (edges)
        for n in visited:
            for nei in n.neighbors:
                newneighbor = mapping[nei]
                mapping[n].neighbors.append(newneighbor)
        
        #4. return new root      
        return mapping[node]
