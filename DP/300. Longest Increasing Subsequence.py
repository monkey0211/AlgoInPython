# - 最长公共子序列: 目的是从某个木桩出发，从前向后，从低往高，看最多能踩多少个木桩。
# - state: f[i] 表示(从任意某个木桩)跳到第i个木桩，以nums[i]结尾的最长上升子序列
#     - 此时需要遍历nums[i]之前的所有nums[j], nums[i]是可以从任意比自己小的nums[j]来:
#     - if nums[j] < nums[i] 更新dp[i] = max(dp[j] + 1, dp[i])
# - initialization: 因为起点不一定是第一个 每一个都可能成为起点 所以要把所有元素初始化(dp[i] = 1)
# - answer: 找的是Max(dp) 而不是dp[i-1] 因为不一定是最后一个 求的是最多
# - eg: [2, 4, 3, 13, 6, 8] 6可以从2,4,3跳过来
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i]) #用来替换初始化的dp[i]
        return max(dp) # 找的是Max(dp) 而不是dp[i-1] 因为不一定是最后一个 求的是最多

        