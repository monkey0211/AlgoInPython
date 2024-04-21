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

