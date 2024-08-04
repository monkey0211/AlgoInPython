class MedianFinder:
    
# heap: O(nlogn)
# left half: maxHeap
# right half: minHeap

    def __init__(self):
        self.left = []
        self.right = []
        
    #如两边元素个数相等 放左边.再左边pop一个最大的换到右边. 此时左<右
    #如左=右+1, 放右边 再pop一个最小的放左边
    #最后两种情况 左==右 or 左 < 右
    #注意正负      
    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heapq.heappush(self.left, -num)
            tmp = heapq.heappop(self.left)
            heapq.heappush(self.right, -tmp)
        else:
            heapq.heappush(self.right, num)
            tmp = heapq.heappop(self.right)
            heapq.heappush(self.left, -tmp)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0])/2.0 
        else:
            return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()