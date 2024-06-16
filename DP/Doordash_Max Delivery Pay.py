from bisect import bisect_right

class Solution:
    # create tuple(start, end, pay) and sort delivery by ending time. 
    # find previous delivery endTime that doens't overlap with current startTime
    # dp[i]: represents the maximum pay we can get up to the i-th delivery.
    def max_delivery_pay(self, start_time, end_time, d_starts, d_ends, d_pays):
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
print(test.max_delivery_pay(start_time, end_time, d_starts, d_ends, d_pays))  # Output: 6
