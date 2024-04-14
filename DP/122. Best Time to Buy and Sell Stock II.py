class Solution:
    # 可以多次交易 问最大profit: 贪心法. 凡是上升 就买入 每次都进行累计 一定会得到最大
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        if len(prices) == 1: return 0

        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i]>=prices[i-1]:
                maxProfit += prices[i]-prices[i-1]
        return maxProfit
        