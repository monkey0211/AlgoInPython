class MedianFinder:

# left half: maxHeap
# right half: minHeap

    def __init__(self):
        self.left = []
        self.right = []

    # |<-------->|<---------->|
    #     left        right
    # left部分和right部分 分别用maxHeap和minHeap维护 每次查找 只找相应的堆顶即可
    # 人为规定right的个数>=left 这样总个数为偶数时:返回(l[0]+r[0])/2.0 奇数时直接返回r[0]    
    # 插入一个新数时 如两边元素个数相等 先放左边 再从左边pop一个最大的换到右边. 此时左<右
    # 如右=左+1(左边比右边少一个) 先放右边 再pop一个最小的放左边
    # 最后两种情况 左==右 or 左<右
    # 注意入堆时元素的正负 最大堆要负号入堆      
    def addNum(self, num: int) -> None:  # 插入操作 log(n)
        if len(self.left) == len(self.right):
            heapq.heappush(self.left, -num)
            tmp = heapq.heappop(self.left)
            heapq.heappush(self.right, -tmp)
        else:
            heapq.heappush(self.right, num)
            tmp = heapq.heappop(self.right)
            heapq.heappush(self.left, -tmp)
        

    def findMedian(self) -> float:  # find是O(1)
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0])/2.0 
        else:
            return self.right[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()