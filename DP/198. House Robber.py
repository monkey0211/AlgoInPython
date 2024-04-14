class Solution:
    # - dp[i] : max money after visiting the house[i] 代表前n个
    # - 不抢dp[i-1] ,抢dp[i-2] + money[i]
    # - time O(n) space O(n) --> rolling空间优化
    # - Rolling Array: 每一个dp的位置都模3. --> 模2也可以: 只需要两个位置
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [0]*(len(nums) + 1)
  
        dp[0] = 0
        dp[1] = nums[0]
        
        for i in range(2, len(dp)): #dp长度比nums多一个
            dp[i] = max(dp[i-2]+nums[i-1], dp[i-1]) 
        return max(dp)
