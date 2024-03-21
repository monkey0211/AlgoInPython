class Solution:
    #构建graph: stop: list of busIndex, 从busIndex又可以用routes[busIndex]得到nextStops
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target: return 0
        visitedBus = set()
        graph = collections.defaultdict(list)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                graph[routes[i][j]].append(i) # i is the busId

        queue = collections.deque([source]) #must be a iterable list
        res = 0
        while queue:
            res += 1
            for i in range(len(queue)):
                currStop = queue.popleft()
                for bus in graph[currStop]:
                    if bus not in visitedBus:
                        visitedBus.add(bus)
                        for nextStop in routes[bus]:
                            if nextStop == target:
                                return res       
                            queue.append(nextStop)
        return -1
