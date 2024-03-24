class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        tmp = []
        self.dfs(res, tmp, n, k, 1)
        return res
    
    def dfs(self, res, tmp, n, k, index):
        if len(tmp) == k:
            res.append(tmp[:])
            return 
        
        for i in range(index, n+1):
            tmp.append(i)
            self.dfs(res, tmp, n, k, i+1)
            tmp.pop()
