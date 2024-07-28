
import collections
class Solution: 
# find minimum given a convex function
# 1. binary search
    def __init__(self, epsilon = 1E-5, maxIterations = 1000, alpha = 0.01):
        self.epsilon = epsilon
        self.maxIterations = maxIterations
        self.alpha = alpha
        
    def convexFunc(self, x):
        return x*x
        
    def findMinimum1(self, left, right):
        while right - left > self.epsilon:
            mid = (left + right) / 2
            midAndEpsilon = mid + self.epsilon
            midValue = self.convexFunc(mid)
            midValueEpsilonValue = self.convexFunc(midAndEpsilon)
            if midValue > midValueEpsilonValue:
                left = mid
            else:
                right = mid 
        return (left + right) / 2
                
#2. gradient descent方法
    def findMinimum2(self, point):
        curPoint = point
        
        for _ in range(self.maxIterations):
            nextPoint = curPoint + self.epsilon
            slope = self.getSlope(curPoint, nextPoint)
            if abs(slope) < self.epsilon:
                break
            curPoint -= self.alpha * slope
          #  print(curPoint)
        return curPoint
    
    def getSlope(self, left, right):
        return (self.convexFunc(right) - self.convexFunc(left))/(right - left)

test = Solution()
print(test.findMinimum1(-10, 10))
print(test.findMinimum2(-1000))
# follow-up: 1. if function is non-convex but unimodal -> we can still use this method.    
        
