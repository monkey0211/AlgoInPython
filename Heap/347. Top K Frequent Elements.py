class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heap = []
        res = []
        if not nums: return []
        counter = collections.Counter(nums)
        for key in counter:
            heapq.heappush(heap, (counter[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap: # heap is same as stack: use while to get elements
            res.append(heapq.heappop(heap)[1])
        return res