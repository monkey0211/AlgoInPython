# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [(ai,aj),(bi, bj), inci] means M[x][y] should be incremented by inci for all ai <= x < aj and bi <= y < bj
# Return 2d matrix after applying all the updates.
class Solution:
    def rangeAddition2D(self, m, n, ops):
        # Initialize the matrix with all 0's
        M = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Apply each operation using the difference array technique
        for op in ops:
            sx, sy = op[0]
            ex, ey = op[1]
            inci = op[2]
            
            M[sx][sy] += inci
            if ex + 1 < m:
                M[ex + 1][sy] -= inci
            if ey + 1 < n:
                M[sx][ey + 1] -= inci
            if ex + 1 < m and ey + 1 < n:
                M[ex + 1][ey + 1] += inci
        
        # Compute the final matrix by propagating the difference values
        # First, propagate vertically
        for i in range(m):
            for j in range(n):
                if i > 0:
                    M[i][j] += M[i - 1][j]
        
        # Then, propagate horizontally
        for i in range(m):
            for j in range(n):
                if j > 0:
                    M[i][j] += M[i][j - 1]
        
        # Remove the extra row and column used for the difference array
        return [row[:n] for row in M[:m]]

# Example usage
# m = 4
# n = 5
# ops = [((1, 1), (3, 4), 2), ((0, 0), (2, 2), 1)]
# test = Solution()
# print(test.rangeAddition2D(m, n, ops))


## if 二维 如果原数组a[][]不为0
#     // [i,j] is start, [x, y] is end
#     void insert(int i, int j, int x, int y, int c)
#     {
#         b[i][j] += c;
#         b[i][y + 1] -= c;
#         b[x + 1][j] -= c;;
#         b[x + 1][y + 1] += c;
#     }

# int main()
# {
#     int n, m, q, x, y, xx, yy, c;

#     // 初始化差分矩阵 return b[][]
#     for (int i = 1; i <= n; i ++ )
#         for (int j = 1; j <= m; j ++ )
#             insert(i, j, i, j, a[i][j]);
    
#     // 处理每个操作ops
#     for (int i = 0; i < q; i ++ )
#     {
#         insert(x, y, xx, yy, c); 
#     }
#     //add to original, return b[][]
#     for (int i = 1; i <= n; i ++ )
#         for (int j = 1; j <= m; j ++ )
#             b[i][j] += b[i][j - 1] + b[i - 1][j] - b[i - 1][j - 1];
# }