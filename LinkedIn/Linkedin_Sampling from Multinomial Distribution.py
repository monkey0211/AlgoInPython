# simulate  M sided diece given the prob of each side showing up
# input: prob pi of showing face i = {1,2..m}
# output: N samples from this dice. random pick N times with above probability

# ref: https://leetcode.com/problems/random-pick-with-weight/description/
# 每一次得到一个sample, run N times.
import math
import random


class Multinomial:
    def __init__(self, pairList): #(face, prob)
        self.pairList = pairList
        
    def getRandomeSample(self):
        
        prefixSum = []*len(self.pairList)
        prefixSum[0] = self.pairList[0][1]
        for i in range(1, len(self.pairList)):
            prefixSum[i] += self.pairList[i][1]
        
        total = prefixSum[-1]
        #归一化
        for i in range(len(prefixSum)):
            prefixSum[i] = prefixSum[i]/total
        
        # find the first index in prefix that >= target: binary search 
        target = random.random() # random.random() 取[0,1)之间的随机数
        index = self.binarySearch(prefixSum, target)
        return self.pairList[index][0] # 返回一次sample的结果
       

    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid 
            else:
                left = mid
        if nums[left] >= target: #先看left, 如果left都大 说明都大
            return left 
        else:
            return right 
    
# Followup:
# 1. how to simulate any distribution
# 2. some pi = 0? 把这个pair从原list里面去掉
# 3. how to implement the batch get? 
# 4. ....TODO
# 10. given a random() which return floating number in [0, 1], 
# return a point(x, y) from a circle with radius R which return tuple(float, float)
# [rcos, rsin] -> R
    def sampleFromCircle(R):
        theta = random * 2 * math.pi
        r = math.sqrt(random()) * R
        return (r * math.cos(theta), r*math.sin(theta))
            
            
            
            
        