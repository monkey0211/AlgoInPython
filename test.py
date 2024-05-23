import collections
import heapq
from typing import List
List.__lt__ = lambda x, y: (x[0] < y[0])
class Solutions:
    def mergeKSortedArray(self, arrs): 
        heap = []
        res = []
        for nums in arrs:
            heapq.heappush(heap, nums)
        
        while heap:
            nums = heapq.heappop(heap)
            res.append(nums[0])
            if 0 < len(nums)-1:   
                nums = nums[1:]
                heapq.heappush(heap, nums)
        return res

test = Solutions()
print(test.mergeKSortedArray([[1,4,5],[1,3,4],[2,6]]))
        