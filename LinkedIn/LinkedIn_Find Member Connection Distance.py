# graph = {"Bob":["Alice","John"],
#          "Alice":["Bob","Frank", "Lucy"],
#          "Frank":["Alice"],
#          "John":["Bob","Jenny"],
#          "Jenny":["John", "Lucy"],
#          "Lucy":["Jenny", "Alice"]}
# 给一个graph 都是member connections. 给出两个member: m1, m2. 找最短路

# 起始点固定的情况可以考虑bi-direction BFS. (可以加速搜索 不能减小复杂度)
# 一个从头搜, 一个从尾搜, 最后如果相交 就直接return steps
class Member:
    def __init__(self):
        pass
    def getName(self):
        pass
    def getMemberId(self):
        pass

class MemberConnections:
    def getConnections(self, member: Member):
        pass

class Solution:
    def getDistance(self, m1, m2):
        # clarify: 1)if no connections 2) if same member(circle) possible. 
        
        if m1 == m2: return 0
        
        queue1 = collections.deque()
        queue1.append((m1, 0))      
        queue2 = collections.deque()
        queue2.append((m2, 0))
        
        step = 0
        visited1 = set()
        visited1.add(m1)
        visited2 = set()
        visited2.add(m2)
        
        while queue1 and queue2:
            step += 1
            hasConnected = False
            # search the smaller size(可能最先走完)
            if len(queue1) < len(queue2):
                hasConnected = self.moveOneStep(queue1, visited1, visited2)
            else:
                hasConnected = self.moveOneStep(queue2, visited2, visited1)
            
            if hasConnected:
                return step
        
        # if no connection found
        return -1
    
    def moveOneStep(self, queue, visited, otherVisited):
        for i in range(len(queue)):
            node = queue.popleft()
            visited.add(node)
            
            for nei in MemberConnections.getConnections(node):
                # 看是否连接上
                if nei in otherVisited:
                    return True
                else:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
                  
        return False

# variance1: 
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

# class Member:
#     def __init__(self):
#         pass
#     def getName(self):
#         pass
#     def getMemberId(self):
#         pass
# class Solution:
#     def __init__(self, graph):
#         self.graph = graph
        
#     def getConnections(self, node):
#         return graph[node]
        
#     def getDistance(self, a, b):
#         queue = collections.deque()
#         queue.append((a, 0))
        
#         path = []
#         step = 0
#         visited = set()
#         visited.add(a)
#         while queue:
#             node, step = queue.popleft()
#             if node == b:
#                 return step 
            
#             for nei in self.getConnections(node):
#                 if nei not in visited:
#                     queue.append((nei, step+1))
#                     visited.add(nei)
                  
#         return -1

# graph = {0:[1,3],
#          1:[0,2,3,4,5],
#          2:[1],
#          3:[0,1,5],
#          4:[1,5,6],
#          5:[1,3,4,6],
#          6:[4,5]}
# test = Solution(graph)
# print(test.getDistance(0, 6))
# print(test.getDistance(1, 5))
        