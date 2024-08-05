class Solution:
# dp[i][j] : min cost if number ith house, paint j color.
# dp[i][j] = min(dp[i-1][j'], dp[i-1][j’’]) + costs[i][j]
# time O(n) space O(n) -->节省空间做法: 直接更新costs[i][j] 这样不占用多余空间
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        dp = costs
        for i in range(1, len(costs)):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        return min(dp[-1])

# Follow up: if we have n Cakes and m colors(n >> m), each color can be used only once(thus not all cakes will be decorated) 
# and the colors have to be used in order
# (eg cake decorated color #i must be to the left of cake decorated color # j if i < j
# 1.return the minimum cost
# 2.if the baking sheet is a loop such that the first cake and last cake are adjacent to each
