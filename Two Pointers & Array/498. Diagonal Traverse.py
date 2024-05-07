class Solution:
    #method 1: use dict[i+j]存每个对角线的元素, 再按%2 reverse取出
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat: return []
        dict = collections.defaultdict(list)
        res = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dict[i+j].append(mat[i][j])
        
        for k in dict.keys():
            values = dict[k]
            if k%2 == 1:
                res.extend(values)
            else:
                res.extend(reversed(values))
        return res

#method2: 先按顺序遍历 k=m+n-1, k为偶数时reverse
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        result = []
        m, n = len(mat), len(mat[0])
        i, j = 0, 0


        for k in range(m+n-1):
            level = []
            if k < n:
                i, j = 0, k
            else:
                i, j = k - n + 1, n - 1 #total is (n-1) cols
            while i < m and j >= 0:
                level.append(mat[i][j])
                i += 1
                j -= 1

            if k % 2 == 0:
                level.reverse()
            result.extend(level)
        return result

        