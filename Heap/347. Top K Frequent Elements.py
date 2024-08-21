class Solution:
    # method 1: heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heap = []
        res = []
        if not nums: return []
        counter = collections.Counter(nums)
        for key in counter:
            if len(heap) < k:
                heapq.heappush(heap, (counter[key], key))
            elif counter[key] > heap[0][0]:
                heapq.heappushpop(heap, (counter[key], key))
        
        while heap: # heap is same as stack: use while to get elements
            res.append(heapq.heappop(heap)[1])
        return res # 如果按顺序就需要reverse

    # method 2: binary search/quick select
    # get the frequent dictionary
        # sort out the k highest value keys
        # use quick sort to find the kth largest element [DO NOT NEED TO SORT THEM ALL]
        # return the left hand side of the Kth largest pivot
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        key = list(freq.keys()) # the number
        val = list(freq.values()) # the frequent

        def partition(nums, left, right,key):
            p = right
            right -=1
            while left <= right:
                while left<=right and nums[left]>=nums[p]:
                    left +=1
                while left <= right and nums[right]<=nums[p]:
                    right -=1
                if left <= right:
                    nums[left],nums[right] = nums[right],nums[left]
                    key[left],key[right] = key[right],key[left]
            
            nums[left], nums[p] = nums[p],nums[left]
            key[left], key[p] = key[p],key[left]
            return left

        def quickSort(nums,left,right):
            if not nums or len(nums)<=1: return nums
            if left >= right: return nums
            p = partition(nums,left,right,key)
            if p == k-1:
                return key[:k]
            elif p > k-1:
                return quickSort(nums, left, p-1)
            else: return quickSort(nums, p+1, right)

        quickSort(val, 0, len(val)-1)
        return key[:k]


import heapq
# 用linked list计算counter方法
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


    def topKFrequent(head: ListNode, k: int) -> list:
        # Step 1: Count the frequency of each element in the linked list
        # 用linked list计算counter
        frequency = collections.defaultdict(int)
        current = head
        
        while current:
            frequency[current.val] += 1
            current = current.next
        
        # Step 2: Use a min-heap to keep track of the top k elements
        min_heap = []
        
        for num, freq in frequency.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            elif freq > min_heap[0][0]:
                heapq.heappushpop(min_heap, (freq, num))
        
        # Step 3: Extract the elements from the heap
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        
        return result

    # # Helper function to create linked list from list of values
    # def create_linked_list(values):
    #     if not values:
    #         return None
    #     head = ListNode(values[0])
    #     current = head
    #     for value in values[1:]:
    #         current.next = ListNode(value)
    #         current = current.next
    #     return head

    # # Test case 1
    # nums = create_linked_list([1, 1, 1, 2, 2, 3])
    # k = 2
    # print(topKFrequent(nums, k))  # Output: [1, 2]

    # # Test case 2
    # nums = create_linked_list([1])
    # k = 1
    # print(topKFrequent(nums, k))  # Output: [1]

    # Aaron version of quick selection approach.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        self.counter = collections.Counter(nums)
        keys = list(self.counter.keys())
        idx = self.partition(keys, k, 0, len(keys)-1)
        return keys[:idx+1]
    
    def partition(self, keys, k, start, end) -> int:
        if start >= end:                                # corner case: keys is empty. start = 0, end = -1
            return start
        left, right = start - 1, end + 1
        # 注意这里pivot意义是频率!key对应原数组中的key的个数 用频率去做partition
        pivot = self.counter[keys[(left + right) // 2]]
        while left < right:
            while True:
                left += 1   # 从左到右 找频率<=pivot的key 放到右边去
                if self.counter[keys[left]] <= pivot:
                    break
            while True:
                right -= 1  # 从右到左 找频率>=pivot的key 放到左边去
                if self.counter[keys[right]] >= pivot:
                    break
            if left < right:  # 注意这里只交换 不再进行指针移动
                keys[left], keys[right] = keys[right], keys[left]
        if k <= right - start + 1: # 区间[start,right] 有right-start+1个数
            return self.partition(keys, k, start, right) # k落在左边
        else:
            return self.partition(keys, k - (right - start + 1), right + 1, end)