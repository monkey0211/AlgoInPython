class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #1. build a graph: defaultdict(set)
        graph = {}
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()
        
        #2. build adjList
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            minLen = min(len(word1), len(word2))
            for j in range(minLen):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break # must have break
            if j == minLen-1 and len(word1) > len(word2) and word1[j] == word2[j]:
                return ""
        
        #3. build indegree
        degree = {x:0 for x in graph}
        for x in graph:
            for neighbor in graph[x]:
                degree[neighbor] += 1

        queue = collections.deque()
        for x in degree:
            if degree[x] == 0:
                queue.append(x)
        res = []
        while queue:
            char = queue.popleft()
            res.append(char)
            for nei in graph[char]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    queue.append(nei)
        return "".join(res) if len(res) == len(graph) else ""
        
