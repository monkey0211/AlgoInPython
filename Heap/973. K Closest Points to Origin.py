class Solution:
    # 解法1: max heap 时间O(nlogk) 空间O(k)
    def kClosest_v1(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            # negate the distance to simulate max heap
            # python默认是小根堆
            dist = -self.squared_distance(points[i])
            # fill the heap with the first k elements of points
            if len(heap) < k:
                heapq.heappush(heap, (dist, i))
            else:
                # If this point is closer than the kth farthest,
                # discard the farthest point and add this one
                # 注意这个if算是一个常数级别的优化 避免多余的heap push/pop Meta有时followup会问
                if dist > heap[0][0]:
                    heapq.heappushpop(heap, (dist, i))
        
        # Return all points stored in the max heap
        ret = []
        for _, idx in heap:
            ret.append(points[idx])
        return ret
    # Calculate and return the squared Euclidean distance.
    def squared_distance(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2
    
    # 解法2: quick select 时间O(n)(amortized) 空间O(1)
    def kClosest_2(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quick_select(points, k)
    
    def quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        left, right = 0, len(points) - 1
        pivot_index = len(points)
        while pivot_index != k:
            # Repeatedly partition the list
            # while narrowing in on the kth element
            pivot_index = self.partition(points, left, right)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1
        
        # Return the first k elements of the partially sorted list
        return points[:k]
    
    def partition(self, points: List[List[int]], left: int, right: int) -> int:
        pivot = points[(left + right) // 2]
        pivot_dist = self.squared_distance(pivot)
        while left < right:
            # Iterate through the range and swap elements to make sure
            # that all points closer than the pivot are to the left
            if self.squared_distance(points[left]) >= pivot_dist:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1
        
        # Ensure the left pointer is just past the end of
        # the left range then return it as the new pivotIndex
        if self.squared_distance(points[left]) < pivot_dist:
            left += 1
        return left