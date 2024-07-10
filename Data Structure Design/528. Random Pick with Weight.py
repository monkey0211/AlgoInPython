# https://www.youtube.com/watch?v=KYmlcich2_k
import random

class Solution:
    def __init__(self, w:List[int]):
        self.prefix_sum = [0] * (len(w))
        self.prefix_sum[0] = w[0]
        for i in range(1, len(w)):
            self.prefix_sum[i] = self.prefix_sum[i-1] + w[i]     
        self.total = self.prefix_sum[-1]

    def pickIndex(self) -> int:
    # find the first index in prefix that >= target: binary search 
    # 在prefix里搜索第一个比target大的数的(index)
    # eg [1,3], prefix区间为[0,1) [1,4) target在两个区间的比例为25%, 75%
        
        target = self.total * random.random() # random.random() 取[0,1)之间的随机数
        left, right = 0, len(self.prefix_sum)-1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.prefix_sum[mid] == target:
                return mid
            elif self.prefix_sum[mid] > target:
                right = mid
            else:
                left = mid
        
        if self.prefix_sum[left] >= target: #先看left, 如果left都大 说明都大
            return left 
        else:
            return right 

#如何测试: 1) fix target 比较output 2)call this multiple times 