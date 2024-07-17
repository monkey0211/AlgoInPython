# Given two arrays representing bus ticket prices for departures and returns, respectively, 
# where the index corresponds to the timestamp (in days) and the value represents the price, 
# the task is to find the minimum cost of purchasing a valid pair of tickets. 
# The return ticket must be for a date on or after the corresponding departure's day.
# For instance, consider the arrays departure = [10, 3, 10, 9, 3] and return = [4, 20, 6, 7, 10]. 
# The minimum cost for a valid pair is 3 + 6 = 9.

class Solution: 
    def minBusTicketCost(self, departure, back):
        minCost = float("inf")
        minReturn = [0]*len(back)
        minReturn[-1] = back[-1] #初始化最后一位
        
        #从右往左遍历return_,创建array记录当前index下的最小值(including itself)
        for i in range(len(back) - 2, -1, -1):
            minReturn[i] = min(back[i], minReturn[i+1])
        
        #从头遍历departure, 当前departure[i]+minReturn[i]就是最小
        for i in range(len(departure)):
            minCost = min(minCost, departure[i] + minReturn[i])
        return minCost
            
            
test = Solution()
departure = [10, 3, 10, 9, 3]
back = [4, 20, 6, 7, 10]
print(test.minBusTicketCost(departure, back))