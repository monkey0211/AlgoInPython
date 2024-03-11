from typing import List

# (连续的可以用二分 每行的第一个数大于上一行的最后一个整数)
# Time O(logmn) space O(1) 二维-->一维
# 已知位置求下标:(坐标关系）
# m, n = len(matrix), len(matrix[0])
# start, end = 0, n * m - 1
# x, y = mid // n, mid % n

class SearchMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            #change number back to cordinates
            midX, midY = mid // n, mid % n
            if matrix[midX][midY] >= target:
                right = mid
            else:
                left = mid

        if matrix[left//n][left%n] == target or matrix[right//n][right%n] == target:
            return True
        return False