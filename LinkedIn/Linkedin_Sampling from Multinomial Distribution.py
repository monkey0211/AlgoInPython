# simulate  M sided diece given the prob of each side showing up
# input: prob pi of showing face i = {1,2..m}
# output: N samples from this dice

import math
import random


class Multinomial:
    def __init__(self, valueProbPairList): #(face, prob)
        self.valueProbPairList = valueProbPairList
        
    def getRandomeSample(self):
        
        prefixSum = []*len(self.valueProbPairList)
        prefixSum[0] = self.valueProbPairList[0][1]
        for i in range(1, len(self.valueProbPairList)):
            prefixSum[i] += self.valueProbPairList[i][1]
        
        total = prefixSum[-1]
        #归一化
        for i in range(len(prefixSum)):
            prefixSum[i] = prefixSum[i]/total
        
        # find the first index in prefix that >= target: binary search 
        target = random.random() # random.random() 取[0,1)之间的随机数
        index = self.binarySearch(prefixSum, target)
        return self.valueProbPairList[index][0]

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
            
            
            
            
        