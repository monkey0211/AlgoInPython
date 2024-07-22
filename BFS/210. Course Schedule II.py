class Solution:
    # 返回任意一个拓扑序. 注意最后结果需要len(res) == numCourses, else []
    # Time O(V + E) Space O(V + E)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        edges = collections.defaultdict(list)

        degree = {x: 0 for x in range(numCourses)}
        queue = collections.deque([])

        for x, y in prerequisites:
            edges[y].append(x)
            degree[x] += 1
        for i in degree:
            if degree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            neighbors = edges[course]
            for n in neighbors:
                degree[n] -= 1
                if degree[n] == 0:
                    queue.append(n)
        return res if len(res) == numCourses else []
    
    # Uber variation: find all paths(DFS)
    def findAllOrders(self, numCourses, prerequisites): 

        graph = collections.defaultdict(list)
        in_degree = [0] * numCourses
        res = []
        visited = [False] * numCourses
        for x, y in prerequisites:
            graph[y].append(x)
            in_degree[x] += 1
        self.dfs(res, graph, in_degree, [], numCourses, visited)
        return res

    def dfs(self, res, graph, in_degree, tmp, n, visited):
        if len(tmp) == n:
            res.append(tmp[:])
            return
        
        for node in range(n):
            if in_degree[node] == 0 and not visited[node]: #对degree为0的每个点遍历
                visited[node] = True
                tmp.append(node)
                for nei in graph[node]: #必须更新每一个neighbor的degree.
                    in_degree[nei] -= 1
                self.dfs(res, graph, in_degree, tmp, n, visited)
                for nei in graph[node]:
                    in_degree[nei] += 1
                tmp.pop()
                visited[node] = False

n = 4
p = [[1,0], [2,0], [3,2], [3,1]]
n = 3
# p = [[1,0], [2,1], [0,2]]
print(findOrder(n, p))