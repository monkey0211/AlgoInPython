class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      
        intervals = sorted(intervals)
        res = []
        for x, y in intervals:
            if not res or res[-1][1] < x:
                res.append([x, y])#不能用tuple, 下面需要更新y值
            else:
                if res[-1][0] <= x <= res[-1][1]: #只有着一种情况需要更新end边界
                    res[-1][1] = max(res[-1][1], y)
        return res
