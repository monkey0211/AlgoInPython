# given list of houses, 如果只有一个router 放在哪里distance最短(distance is MSE): mean of houses
# sum(xi - r)^2 -> gradient is zero
#如果有两个router, 

# 先求prefix Distance
from typing import List
class Solution:
    def getPrefixSum(self, houses):
        prefix = []
        curTotal = 0
        curSquareTotal = 0
        for i in range(len(houses)):
            curTotal += houses[i]
            curSquareTotal += houses[i]**2 #先平方再和
            curMean = curTotal/(i+1) #这个就是一个r时候的最优位置(mean)
            # 前i个房子和router的距离和 sum(xi - r)^2展开. 
            curDistance = curSquareTotal + (i+1)*curMean**2 - 2*curMean*curTotal
            prefix.append(curDistance)
        
        return prefix

    # 两个router的时候, 先正向计算prefix, 再reverse计算prefix, 然后对比叠加计算min.
    def getOptimalRoutersDistance(self, houses: List[int]):
        prefixSum = self.getPrefixSum(houses)
        houses.reverse()
        reversePrefixSum = self.getPrefixSum(houses)
        reversePrefixSum.reverse()
        
        minDist = reversePrefixSum[0]
        for i in range(1, len(houses)):
            curDist = prefixSum[i-1] + reversePrefixSum[i]
            minDist = min(curDist, minDist)
        return minDist
        
test = Solution()
print(test.getOptimalRoutersDistance([4,8,12,18]))
    
    
    
    
    
    
    
    