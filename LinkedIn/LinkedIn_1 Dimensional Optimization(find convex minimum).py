
import collections
class Solution: 
# find minimum given a convex function
# if given array, please see: https://github.com/monkey0211/AlgoInPython/blob/main/Binary%20Search/Meta%20Find%20Local%20Min%20Element.py
# 1. binary search: given a function and left, right
# time o(log2(L/e)), L is r-l.
    def __init__(self, epsilon = 1E-5, maxIterations = 1000, alpha = 0.01):
        self.epsilon = epsilon
        self.maxIterations = maxIterations
        self.alpha = alpha
        
    def convexFunc(self, x):
        return x*x
        
    def findMinimum1(self, left, right):
        while right - left > self.epsilon:
            mid = (left + right) / 2
            midAndEpsilon = mid + self.epsilon #如果是整数 可以直接用nums[mid+1]
            midValue = self.convexFunc(mid)
            midValueEpsilonValue = self.convexFunc(midAndEpsilon)
            if midValue > midValueEpsilonValue:
                left = mid
            else:
                right = mid 
        return (left + right) / 2
                
#2. followup: if input is just a convex function and a random point
    def findMinimum2(self, point):
        curPoint = point
        
        for _ in range(self.maxIterations):
            nextPoint = curPoint + self.epsilon
            slope = self.getSlope(curPoint, nextPoint)
            if abs(slope) < self.epsilon:
                break
            curPoint -= self.alpha * slope
        return curPoint 
    
    def getSlope(self, left, right):
        return (self.convexFunc(right) - self.convexFunc(left))/(right - left)

test = Solution()
print(test.findMinimum1(-10, 10))
print(test.findMinimum2(-1000))
# follow-up: 1. if function is non-convex but unimodal -> we can still use this method.    
# 2. generalize to N>1 dimension?
# how does complexity grow with dimention N?  线性增长 O(T)->O(TN)
