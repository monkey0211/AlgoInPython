# 条件：每一行从小到大 每一列从小到大. 不保证上一行都小于下一行. 因此不能保证比a[i][j]小的都在左上
# 双指针linear search: 从右上角开始，往左下角逼近。不是二分法!. 
# **time O(m+n) space O(1)**
# time 不是m*n 因为vertical只遍历一次 horizontal也只遍历一次
from typing import List
class SearchMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        i, j = 0, len(matrix[0]) - 1
        while i <= len(matrix) - 1 and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

        