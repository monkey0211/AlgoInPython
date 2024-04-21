class Solution:
    # 求: max meeting room required at same time. 求最大重叠room
    # 按时间切片, start的时间+1, end的时间-1. sort之后计算任意时刻哪里取到了最大
    # time O(nlogn) space O(n)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = []
        for start, end in intervals:
            points.append((start, 1))
            points.append((end, -1))
        points = sorted(points)

        room = 0
        maxRoom = 0
        for time, score in points:
            room += score
            maxRoom = max(maxRoom, room)
        return maxRoom
        