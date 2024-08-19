class Solution:
    # Time o(nlogn) for sorting, Space o(1)
    # if current interval does not overlap with the previous: append it.
    # else, if overlap: update previous ending to be max(current, previous)
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

    # Aaron version
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals = sorted(intervals)

        cur_left, cur_right = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > cur_right:
                ret.append([cur_left, cur_right])
                cur_left, cur_right = intervals[i][0], intervals[i][1]
            else:
                cur_right = max(cur_right, intervals[i][1])
        ret.append([cur_left, cur_right])
        return ret