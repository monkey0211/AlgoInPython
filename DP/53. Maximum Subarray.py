class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #prefixSum表示以当前nums[i]结尾的前n个sum, prefixSum - minSum[i-1] 就是以nums[i]结尾的最大的subarray
        #prefix_sum记录前i个数的和，maxSum记录全局最大值，minSum记录前i个数中0-k的最小值
        prefixSum = 0

        if not nums: return 0
        if len(nums) == 1: return nums[0]
        minSum, maxSum = 0, -inf #minSum得为0

        for i in range(len(nums)):
            prefixSum += nums[i] 
            maxSum = max(maxSum, prefixSum - minSum) #minSum得初始化为0  
            minSum = min(prefixSum, minSum) # min_Sum记录前i个数中0-nums[i]的最小值
        return maxSum
        