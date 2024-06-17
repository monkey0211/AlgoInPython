class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        minDist = float("inf")
        for i in range(len(points)):
            cx, cy = points[i]
            if cx == x or cy == y:
                dist = abs(cx-x) + abs(cy-y)
                if dist < minDist:
                    minDist = dist
                    res = i
        return res
        