# 记住DFS的每层return 返回值必须一致(一般就是要求的output)
# 一般无返回值 但是如果要求判断是否 需要return T/F
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        return self.dfs(wordDict, s, {}) # 这里要加上return
    
    def dfs(self, wordDict, remaining, memo):
        if remaining in memo:
            return memo[remaining]
        if s in wordDict:
            memo[remaining] = True
            return True     

        for i in range(len(remaining)):
            left = remaining[:i]
            right = remaining[i:]
            if right in wordDict and self.dfs(wordDict, left, memo):
                memo[remaining] = True
                return True #这里直接return True 因为是找任意解 找到就返回 不用再搜了
        memo[remaining] = False

