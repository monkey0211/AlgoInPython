from sortedcontainers import SortedDict
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
    # 删除接口复杂度: O(klogn) n:现有区间数量 k:与要移除区间重叠的区间数量
    def removeInterval(self, start, end):
        index = self.intervals.bisect_left(start)
        to_add = [] # 记录remove之后被拆分出来的新的interval

        # 查找并移除重叠部分
        while index < len(self.intervals):
            curr_start, curr_end = self.intervals.peekitem(index)
            # 当前区间起点已在end之后->后面不会再有重叠 退出while
            if curr_start >= end:
                break
            # 当前区间的终点在start之前 也不会有overlap 得往后接着看
            if curr_end <= start:
                index += 1 # 这里记得+1 否则死循环
                continue

            self.length -= min(end, curr_end) - max(start, curr_start)
            # 当前区间起点小于start 需保留前半部分
            if curr_start < start:
                to_add.append((curr_start, start))
            # 当前区间终点大于end 需保留后半部分
            if curr_end > end:
                to_add.append((end, curr_end))
            # 删除当前区间 index指向这轮删除当前区间后的 下一个可能重叠的区间
            del self.intervals[curr_start]
            index = self.intervals.bisect_left(start)

        # 插入由于删除操作产生的 小的新区间
        for new_start, new_end in to_add:
            self.intervals[new_start] = new_end


# compare merge-in-add vs. calculate-in-get

# unit test
i1 = Intervals()
i1.addInterval(3, 6)
i1.addInterval(8, 9)
i1.addInterval(1, 5)
lenth1 = i1.totalCoveredLength() # 6
print(lenth1)

i2 = Intervals()
i2.addInterval(1, 3)
i2.addInterval(2, 3)
i2.addInterval(4, 5)
i2.addInterval(1, 9)
lenth2 = i2.totalCoveredLength() # 8
print(lenth2)