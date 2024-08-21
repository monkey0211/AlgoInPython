import heapq
from typing import List
# heap: silimar to LC23: https://leetcode.com/problems/merge-k-sorted-lists/submissions/1219672656/
# need to re-write comparator: 
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
            if len(nums)-1 > 0:   
                nums = nums[1:]
                heapq.heappush(heap, nums)
        return res

test = Solutions()
print(test.mergeKSortedArray([[1,4,5],[1,3,4],[2,6]]))
        