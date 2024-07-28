class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = nums[0]
        minP = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxP, minP = minP, maxP # 交换正负, 这样保证小的maxP*负数->大的
            maxP = max(nums[i], maxP * nums[i])
            minP = min(nums[i], minP * nums[i])

            res = max(res, maxP)
        return res
        