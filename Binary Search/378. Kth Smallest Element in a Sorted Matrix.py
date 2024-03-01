from typing import List
class KthSmallest:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return -1

        left, right = matrix[0][0], matrix[-1][-1]
        while left + 1 < right:
            mid = (left + right) // 2

            if self.countLessOrEqualTo(matrix, mid) < k:
                left = mid
            else:
                right = mid
        #need to check and easy to check smaller than k, rest is larger than k.
        if self.countLessOrEqualTo(matrix, left) == k:
            return left
        if self.countLessOrEqualTo(matrix, left) < k:
            return right
        else:
            return left
    #two pointer. 
    #count时从左下开始 如果matrix[row][col]小 它上面的所有都小 cnt += row+1
    def countLessOrEqualTo(self, matrix, mid):
        i, j = len(matrix) - 1, 0
        cnt = 0
        while i >= 0 and j <= len(matrix[0]) - 1:
            if matrix[i][j] > mid:
                i -= 1
            else:
                cnt += i + 1
                j += 1
        return cnt
