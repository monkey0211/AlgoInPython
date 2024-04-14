class Solution:
    # 同LC300. LIS(可用dp 可用dfs+memo): https://leetcode.com/problems/longest-increasing-subsequence/
    # 滑雪问题: 起点是极小值 非顺序型(没有左上或者右下的起点) -->适合用记忆化搜索
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        res = 0
        memo = {}
        path = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, self.dfs(path, matrix, i, j, memo))    #取global Max
        return res
    def dfs(self, path, matrix, x, y, memo):
        if (x, y) in memo: return memo[(x, y)]
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return 0
        path = 1 #每层path都需要初始化为1, 否则会从上一层被带入: 如果没找到是一个新的matrix[i][j]就是1

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for index in range(4):
            newx = x + dx[index]
            newy = y + dy[index]
            if 0 <= newx < len(matrix) and 0 <= newy < len(matrix[0]) and matrix[newx][newy] > matrix[x][y]:
                path = max(path, self.dfs(path, matrix, newx, newy, memo) + 1)
        memo[(x,y)] = path
        return path
        
