class Solution:
# 给出 *n*，问由 1...*n* 为节点组成的不同的二叉查找树有多少种？
# 棵树由根节点，左子树和右子树构成。 
# 对于目标n，根节点可以是1, 2, ..., n中的任意一个，假设根节点为k，
# 那么左子树的可能性就是numTrees(k-1)种，右子树的可能性就是numTrees(n-k)种，
# 他们的乘积就根节点为k时整个树的可能性。把所有k的可能性累加就是最终结果
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1) #初始化必须都是0(后面需要叠加)

        for i in range(n+1):
            if i == 0 or i == 1:
                dp[i] = 1           
            else:
            # 举例子: dp[4] = dp[0] * dp[3] + dp[1] * dp[2] + dp[2] * dp[1] + dp[3] * dp[0]
                for j in range(i):
                    dp[i] += dp[j] * dp[i-j-1]
        return dp[n]