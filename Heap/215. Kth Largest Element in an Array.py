class Solution:
    # method 1: heap. time O(nlogk) space o(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        heap = []
        import heapq
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)

    #method 2: quick select(no need to sort) Time: O(n), worst O(n^2). Space O(1)
    # 初始pivot是nums[left]. move all elements smaller than pivot to it’s left, move all elements larger than pivot to it’s right.
    # 最后return nums[k]


    def findKthLargest(self, nums: List[int], k: int) -> int:

        k = len(nums) - k
        return self.partition(0, len(nums) - 1, k, nums)

    def partition(self, start, end, k, nums):
        left, right = start, end #需要重新assign, 因为left right指针会移动
        pivot = nums[left]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 结束的时候left在右 right在左[start, right, left, end]
        # 如果第k小在右侧，搜索右边的范围，否则搜索左侧。不需要全部sort
        if k >= left:
            self.partition(left, end, k, nums)
        if k <= right:
            self.partition(start, right, k, nums)
        return nums[k]