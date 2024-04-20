class Solution:
    # dp[i][j]: the length of their longest common subsequence ending with text1[0:i] text2[0:j]
    # dp[][]比text1/text2多一行一列
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0
        dp = [[0]*(len(text2)+1) for i in range(len(text1)+1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])): 
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
