import heapq
class Solution:
    # heap: 按processingTime放入. 当当前时间>task start time时, 可以把这些task放入heap
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # 需要先按开始时间sort, 但是sort之前需要先记住index, 所以把index也加入每个task tuple里: (start, procTime, index)
        for i, task in enumerate(tasks):
            task.append(i)
        tasks = sorted(tasks, key = lambda x: x[0])

        res = []
        time = 0
        heap = []
        i = 0
        while heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2])) #heap里只需要放procTime, index
                i += 1
            if not heap:
                time = tasks[i][0] #no tasks is processing and CPU idle, so reset time to be the next task
            else:
                procTime, index = heapq.heappop(heap)
                time += procTime
                res.append(index)
        return res


        