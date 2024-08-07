# You are given an m x n matrix M initialized with all 0's and an array of operations ops, 
# where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
# Count and return the number of maximum integers in the matrix after performing all the operations.
class Solution:
    #取最大值 就是看所有operation的交集的范围, 只需要找所有结束operation(i, j)的最小
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minX = m
        minY = n
        for x, y in ops:
            minX = min(x, minX)
            minY = min(y, minY)
        return minX*minY
        