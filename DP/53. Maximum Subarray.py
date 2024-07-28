class Solution:
    #包含正负数
    #prefixSum表示以当前nums[i]结尾的前n个sum, prefixSum - minSum[i-1] 就是以nums[i]结尾的最大的subarray
    #prefix_sum记录前i个数的和，maxSum记录全局最大值(求的结果)，minSum记录前i个数中0-nums[i]的最小值
    
    def maxSubArray(self, nums: List[int]) -> int:
        prefixSum = 0

        if not nums: return 0
        if len(nums) == 1: return nums[0]
        minSum, maxSum = 0, -inf #minSum得为0, 目的是为了截断(如果有负数的话 直接截断, 算为0)
        for i in range(len(nums)):
            prefixSum += nums[i] 
            maxSum = max(maxSum, prefixSum - minSum) # 要的结果: global max
            minSum = min(prefixSum, minSum) # min_Sum记录前i个数中0-nums[i]的最小值
        return maxSum
    
# follow up: 
# 1. what if the list is infinite stream, and you need to report the max sum/product so far?
# 2. what if you are given a directed graph