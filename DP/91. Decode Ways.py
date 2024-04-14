class Solution:
    # DP: 状态转移需要: dp[i-1] + dp[i-2] (if they are valid)
    # python can use compare operator to compare string. eg "0"<"9"
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": # 如果第一个是“0” 需要特判=0 不能从dp[0]转移
            return 0
        if not s: return 0
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            if "1" <= s[i-1] <= "9":
                dp[i] += dp[i-1]
            if "10"<=s[i-2:i] <= "26":
                dp[i] += dp[i-2]
        return dp[-1]

        