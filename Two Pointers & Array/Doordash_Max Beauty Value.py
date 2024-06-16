# graph节点为tourism sites， 边为从site 到site的双向路径， 可以有环。
# 每个site有一个beauty value。从指定的点出发，求给定步数k内的最大累计beauty 值。 
# 同一个景点如果反复经过的话beauty值只能累积一次
import collections
class Solution:
    def maxBeautyValue(self, sites, values, start, k):
        adjList = collections.defaultdict(list)
        visited = set()
        memo = {}
        for x, y in sites:
            adjList[x].append(y)
            adjList[y].append(x)
        for value in values:
            if value == start:
                visited.add(start)  
                return values[start] + self.dfs(start, adjList, k, visited, memo, values)    
        return 0

    def dfs(self, node, adjList, stepsLeft, visited, memo, values):
        if stepsLeft == 0:
            return 0
        if (node, stepsLeft, visited) in memo: return memo[(node, stepsLeft, visited)]
        maxValue = 0
        for nei in adjList[node]:
            if nei not in visited:
                visited.add(nei)
                maxValue = max(maxValue, values[nei] + self.dfs(nei, adjList, stepsLeft - 1, visited, memo, values))
                visited.remove(nei)
            else:
                maxValue = max(maxValue, self.dfs(node, adjList, stepsLeft - 1, visited, memo, values))
        memo[(node, stepsLeft, visited)] = maxValue
        return maxValue
            
        