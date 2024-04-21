class Solution:
    # time O(nlogn) space O(n)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        points = []
        for start, end in intervals:
            points.append((start, 1))
            points.append((end, -1))
        
        points = sorted(points)

        score = 0
        for x, y in points:
            score += y
            if score == 2:
                return False
        return True
