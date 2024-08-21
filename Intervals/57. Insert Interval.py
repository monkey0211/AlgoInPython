class Solution:
    #先insert 用list.insert(index, value), 再merge intervals(LC56)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]

        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[0]>=newInterval[0]:
                intervals.insert(i, newInterval) #list.insert(index, value)
            else:
                intervals.append(newInterval)
        
        res = []
        for i in range(len(intervals)):
            x, y = intervals[i]
            if not res or res[-1][1] < x:
                res.append([x, y])
            else:
                if res[-1][0]<= x <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], y)
        return res

    # 另一种写法 复杂度与上面的相同 just in case有人对list.insert(index, value)复杂度有疑问
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        # Case 1: No overlapping before merging intervals
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Case 2: Overlapping and merging intervals
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Case 3: No overlapping after merging newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
