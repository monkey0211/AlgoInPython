class Solution:
    #DFS+memo: 
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        intervals = zip(startTime, endTime, profit) # zip to put all three as tuples together
        intervals = sorted(intervals) # sort by startTime
        res = 0
        memo = {}
        return self.dfs(0, memo, res, intervals)

    def dfs(self, i, memo, res, intervals):
        # 遍历到最后一个
        if i == len(intervals):
            return 0
        if i in memo: return memo[i]

        # if dont include this one
        res = self.dfs(i+1, memo, res, intervals)

        # if include this one: next interval should be non-overlapping
        
        # j = i + 1
        # while j < len(intervals):
        #     if intervals[i][1] <= intervals[j][0]:
        #         break
        #     j += 1
        #j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
        j = self.binarySearch(intervals, intervals[i][1])
        memo[i] = max(res, intervals[i][2] + self.dfs(j, memo, res, intervals))
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

        