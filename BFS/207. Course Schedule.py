class Solution:
    #  判断是否可以完成所有课程
    # Time O(V + E) Space O(V + E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = {i: 0 for i in range(numCourses)}
        edges = collections.defaultdict(list) # adj_list
        for i, j in prerequisites:
            edges[j].append(i)
            degree[i] += 1
        
        queue = collections.deque()
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for nei in edges[course]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    queue.append(nei)
        return len(res) == numCourses