from sortedcontainers import SortedDict
# i = Intervals()
# i.addInterval(3, 6)
# i.addInterval(8, 9)
# i.addInterval(1, 5)
# i.totalCoveredLength() -> 6

# 1) array.insert()在 number of intervals small的时候可以用, 更efficient(memory continuous).但是需要二分
# 2) 两种方式: 边insert边merge, 先insert再merge 

class Intervals:
    # o(logN) for addInterval
    # o(1) for get total length
    # o(N) in space
    def __init__(self):
        # 使用有序字典保存区间起点和终点 intervals[start] = end
        self.intervals = SortedDict()
        self.length = 0
        
        # followup1: 保存每种颜色的区间及其覆盖长度
        # self.color_intervals = {}
        # self.total_lengths = {}
        
    def addInterval(self, start, end):
        if start >= end:
            return  # 无效区间，不做处理

    # followup1: if add color: 初始化对应颜色的字典和长度
    # def addInterval(self, start, end, color):
        # if color not in self.color_intervals:
        #     self.color_intervals[color] = SortedDict()
        #     self.total_lengths[color] = 0

        # intervals = self.color_intervals[color]
        # total_length = self.total_lengths[color]
        
        # 查找插入位置: 二分
        insertIndex = self.intervals.bisect_left(start)
        
        # 检查是否有重叠区间需要合并: 
        # 先看previous的interval, 比较prev_end and start
        if insertIndex != 0:
            prev_start, prev_end = self.intervals.peekitem(insertIndex - 1)
            
            # eg. [1,9] [4,8]
            if prev_end >= start:
                start = min(start, prev_start)
                end = max(end, prev_end)
                insertIndex -= 1
                self.length -= prev_end - prev_start
                del self.intervals[prev_start]
        
        # 再看后面的interval, 比较curr_start and end
        while insertIndex < len(self.intervals):
            curr_start, curr_end = self.intervals.peekitem(insertIndex)
            # eg.[4,8] [7, 11]
            if curr_start > end:
                break
            end = max(end, curr_end)
            self.length -= curr_end - curr_start
            del self.intervals[curr_start]
        
        # 插入新的（合并后）区间
        self.intervals[start] = end
        # update total length.
        self.length += end - start
        
        # followup1:更新颜色的总覆盖长度
        # self.total_lengths[color] = total_length
        
    def totalCoveredLength(self):
        return self.length
    
    # followup1:
    # def totalCoveredLength(self, color=None):
    #     if color:
    #         return self.total_lengths.get(color, 0)
    #     else:
    #         return sum(self.total_lengths.values())
    
    # followup2: provide a removeInterval(start, end) method which will remove all coverage between start and end.
    def removeInterval(self, start, end):
        index = self.intervals.bisect_left(start)
        to_add = [] # 记录remove之后被拆分出来的新的interval

        # 查找并移除重叠部分
        while index < len(self.intervals):
            curr_start, curr_end = self.intervals.peekitem(index)
            if curr_start >= end:
                break
            if curr_end <= start:
                index += 1
                continue

            self.length -= min(end, curr_end) - max(start, curr_start)

            if curr_start < start:
                to_add.append((curr_start, start))
            if curr_end > end:
                to_add.append((end, curr_end))
            
            del self.intervals[curr_start]
            index = self.intervals.bisect_left(start)

        # 重新插入未被覆盖的部分
        for new_start, new_end in to_add:
            self.intervals[new_start] = new_end


# compare merge-in-add vs. calculate-in-get