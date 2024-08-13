class Solution:
    # DFS: input无重复元素, output可以重复(dfs从当前i继续开始)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        res = []
        tmp = []
        self.dfs(candidates, target, 0, res, tmp)
        return res
    def dfs(self, candidates, remainingTarget, index, res, tmp):
        if remainingTarget == 0: 
            res.append(tmp[:])
            return
        if remainingTarget < 0: #必须有剪枝
            return

        for i in range(index, len(candidates)):
            tmp.append(candidates[i])
            self.dfs(candidates, remainingTarget - candidates[i], i, res, tmp) 
            #答案里可以有重复元素 所以需要从i开始
            tmp.pop()
        