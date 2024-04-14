class Solution:
    #dp: 如果当前prices[i]>minPrice, 更新max, else 更新min. 
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        minPrice = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i]> minPrice:
                maxProfit = max(maxProfit, prices[i] - minPrice)
            else:
                minPrice = min(minPrice, prices[i])
        return maxProfit

        