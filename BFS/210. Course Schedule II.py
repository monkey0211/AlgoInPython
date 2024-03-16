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
        