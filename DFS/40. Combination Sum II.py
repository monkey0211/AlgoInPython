class Solution:
    # output: no duplicate
    # input: can be duplicate. dfs里需要去重if nums[i] == nums[i-1]
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        candidates = sorted(candidates)
        res = []
        tmp = []
        self.dfs(res, tmp, candidates, target, 0)
        return res
    
    def dfs(self, res, tmp, candidates, remainingTarget, index):
        if remainingTarget == 0:
            res.append(tmp[:])
            return
        if remainingTarget < 0:
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            tmp.append(candidates[i])
            self.dfs(res, tmp, candidates, remainingTarget - candidates[i], i+1)
            tmp.pop()
        