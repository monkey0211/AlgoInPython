class Solution:
# DP: 接龙 找最少有多少个square组成. dp[i]: 在前i个中 最小有多少个perfect square
# - 找dp[i]是从哪来的: dp[i] can be generized as i-j*j + j*j, so candidate answer is dp[i-j*j]
#       0 1 2 3 4 5 6 7 8 9 ...
# dp = [0,0,0,0,1,0,0,0,0,1,...]
# - **time O(n*sqrt(n)) space O(n)**
    def numSquares(self, n: int) -> int:
        if n == 1: return 1

        dp = [n+1]*(n+1) #initialize MAX value
        dp[0] = 0 #这里是0 是为了处理整除的情况 eg dp[4] = dp[0] + 1 = 1
        for i in range(1, n+1):
            for j in range(1, int(sqrt(i))+1): #防止dp[i-j*j] out of range.
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[n]