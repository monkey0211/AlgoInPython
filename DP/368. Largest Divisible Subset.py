#动态规划也可以记录解(一般只能记录最优方案/方案个数). 但是只能记录最优的一个方案, 无法记录所有方案.
#dp: 首先排序,dp[i]代表以nums[i]为最大元素的序列最多有多少个。 然后只要nums[j]%nums[i]=0，则可尝试往dp[i]转移, 
# 如需要方案数 则可以直接取max. 如果要记录一个方案, 需要用另一个pre数组记录之前的每一步
# eg. [1,2,4,8] 8 is multiple of 4, then is multiple of 2. 倍数是可以传递的

# time O(n^2) space O(n)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        maxValue = 0

        nums = sorted(nums)
        dp = [1]*len(nums)
        pre = [-1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j]== 0:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        pre[i] = j
        # if need to get max
        #         if nums[i] % nums[j]== 0:
        #             dp[i] = max(dp[j]+1, dp[i])
        # return max(dp)

        #记录最后找到Max时的index
        
            if dp[i] > maxValue:
                maxValue = dp[i]
                maxIndex = i
        #用一个数组记录之前的一步是什么 pre[i] = j, 然后把所有的pre连在一起就是走过的路径
        #return all previous result and connect to one array
        res = []
        for i in range(maxValue):
            res.append(nums[maxIndex])
            maxIndex = pre[maxIndex]
        return res

            
        