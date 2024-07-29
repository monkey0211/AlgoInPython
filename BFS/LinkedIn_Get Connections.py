# Calling getConnections(1) returns the set of IDs for users {0, 2, 3, 4, 5}. getConnections(6) returns the set of IDs for users {4, 5}.
# Sample expected outputs:
# getDistance(0,6) => 3
# getDistance(1,5) => 1
# Graph edges:
# {
#   0: [1,3],
#   1: [0,2,3,4,5],
#   2: [1],
#   3: [0,1,5],
#   4: [1,5,6],
#   5: [1,3,4,6],
#   6: [4,5]
# }
# Input / Output
# Input: two integer IDs userA and userB representing nodes in the graph.
# Output: the length of the shortest path between userA and userB.
import collections

class Solution:
    def __init__(self, graph):
        self.graph = graph
        
    def getConnections(self, node):
        return graph[node]
        
    def getDistance(self, a, b):
        queue = collections.deque()
        queue.append((a, 0))
        
        path = []
        step = 0
        visited = set()
        visited.add(a)
        while queue:
            node, step = queue.popleft()
            if node == b:
                return step 
            
            for nei in self.getConnections(node):
                if nei not in visited:
                    queue.append((nei, step+1))
                    visited.add(nei)
                  
        return -1

graph = {0:[1,3],
         1:[0,2,3,4,5],
         2:[1],
         3:[0,1,5],
         4:[1,5,6],
         5:[1,3,4,6],
         6:[4,5]}
test = Solution(graph)
print(test.getDistance(0, 6))
print(test.getDistance(1, 5))
        