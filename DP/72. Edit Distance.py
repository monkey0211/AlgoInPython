# dp[i][j]表示word1的前i个字符最少要用几次编辑可以变成word2的前j个字符
# 序列型一般会定义dp为前几个
#    dp[i - 1][j] --> dp[i][j]代表add一个字母
#    dp[i][j - 1] --> dp[i][j]代表delete一个字母
#    dp[i - 1][j - 1] --> dp[i][j]代表replace一个字母

# Time O(l1*l2) Space O(l1*l2)—> if rolling array: space O(min(l1,l2))
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n + 1) for i in range(m + 1)] # Add one more row+col.

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]: # 如果最后两个字母相同 不需要转变 注意word和dp的index不同(eg "abc" & "dc" 最后一个字母相同时 等价于“ab"&"d"的比较)
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[m][n]
        # 如果节省空间做法: rolling array.只需要两行 每行(n+1)个
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if word1[i - 1] == word2[j - 1]:
        #             dp[i % 2][j] = min(dp[(i-1) % 2][j-1], dp[(i-1) % 2][j] + 1, dp[i % 2][j-1] + 1)
        #         else:
        #             dp[i % 2][j] = min(dp[(i-1) % 2][j-1], dp[(i-1) % 2][j], dp[i % 2][j-1]) + 1
        # return dp[m % 2][n]
        