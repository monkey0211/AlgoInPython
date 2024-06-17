from bisect import bisect_right
# ref LC1235: https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
class Solution:
    # method 1: DFS + memo. dfs: max payment we can get until i-th delivery
    # create tuple(start, end, pay) and sort delivery by ending time. 
    # find previous delivery endTime that doens't overlap with current startTime
    # time O(nlogn) space O(n)
    def max_delivery_pay1(self, start_time, end_time, d_starts, d_ends, d_pays):
        # Filter deliveries to be within the given time window
        deliveries = []
        for i in range(len(d_starts)):
            if d_starts[i] >= start_time and d_ends[i] <= end_time:
                deliveries.append((d_starts[i], d_ends[i], d_pays[i]))
        
        # Sort deliveries by end time
        deliveries.sort(key=lambda x: x[1])
        res = 0
        memo = {}
        return self.dfs(0, memo, res, deliveries)
    
    def dfs(self, i, memo, res, deliveries):
        # 遍历到最后一个
        if i == len(deliveries):
            return 0
        if i in memo: return memo[i]

        # if dont include this one
        res = self.dfs(i+1, memo, res, deliveries)

        # if include this one: next interval should be non-overlapping
        # j = i + 1
        # while j < len(deliveries):# and deliveries[i][1] > deliveries[j][0]:
        #     if deliveries[i][1] <= deliveries[j][0]:
        #         break
        #     j += 1
        
        # Find the next delivery that starts after the current one end
        # j = bisect.bisect(deliveries, (deliveries[i][1], -1, -1))
        j = self.binarySearch(deliveries, deliveries[i][1])
        memo[i] = max(res, deliveries[i][2] + self.dfs(j, memo, res, deliveries))
        res = memo[i]
        return res
    
    def binarySearch(self, intervals, target):
        left, right = 0, len(intervals)
        while left + 1 < right:
            mid = (left + right) // 2
            if intervals[mid][0] < target: # mid < target
                left = mid
            else:
                right = mid
        if intervals[left][0] >= target:
            return left
        else:
            return right

    # method 2: DP
    # create tuple(start, end, pay) and sort delivery by ending time. 
    # find previous delivery endTime that doens't overlap with current startTime
    # dp[i]: represents the maximum pay we can get up to the i-th delivery.
    def max_delivery_pay2(self, start_time, end_time, d_starts, d_ends, d_pays):
        # Filter deliveries to be within the given time window
        deliveries = []
        for i in range(len(d_starts)):
            if d_starts[i] >= start_time and d_ends[i] <= end_time:
                deliveries.append((d_starts[i], d_ends[i], d_pays[i]))
        
        # Sort deliveries by end time
        deliveries.sort(key=lambda x: x[1])
        # Initialize DP array
        n = len(deliveries)
        dp = [0] * (n + 1)
        
        # List of end times for binary search
        end_times = [deliveries[i][1] for i in range(n)]
        
        for i in range(1, n + 1):
            start, end, pay = deliveries[i-1]
            
            # Find the previous delivery that ends before the current one start
            j = bisect_right(end_times, start) - 1
            
            # Calculate the maximum pay considering or not considering the current delivery
            dp[i] = max(dp[i-1], pay + (dp[j+1] if j != -1 else 0))
        
        return dp[n]

# Example usage
start_time = 0
end_time = 10
d_starts = [2, 3, 5, 7]
d_ends = [6, 5, 10, 11]
d_pays = [5, 2, 4, 1]
test = Solution()
print(test.max_delivery_pay1(start_time, end_time, d_starts, d_ends, d_pays))  # Output: 6

    # def minTaskTime(self, tasks):
    #     # Sort deliveries by end time
    #     tasks.sort(key=lambda x: x[1])
    #     currentEndTime = 0
    #     for startTime, endTime in tasks:
    #         #如果当前结束时间小于等于当前任务的开始时间, 则开始处理
    #         if currentEndTime <= startTime:
    #             currentEndTime = endTime
    #         # 否则需要等待当前任务结束才能开始处理
    #         else:
    #             currentEndTime = max(currentEndTime, endTime)
    #     return currentEndTime
        