class Solution:
    # 注意如果所有点的距离都是unique的: 可用dict, 否则不能去重用其他结构即可(eg. list)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points: return []
        if k >= len(points): return points
        newpoints = []
        res = []
        heap = []

        for (x, y) in points:
            distance = sqrt(x**2 + y**2)
            newpoints.append((x, y, distance))
        
        import heapq
        for (x, y, distance) in newpoints:
            heapq.heappush(heap, (-distance, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            pop = heapq.heappop(heap)
            res.append([pop[1], pop[2]])
        return res
        