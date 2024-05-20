# 记住DFS的每层return 返回值必须一致(一般就是要求的output)
# 一般无返回值 但是如果要求判断是否 需要return T/F
class Solution:
    
     # dfs + memo: dfs为每个切分点切出来的部分remaining is T or F
        # dfs: forloop the separation point, separate string into left, right. 
        # if left in wordDict + self.dfs(right): return True + memo[remaining] = True
 
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s: return False
        wordDict = set(wordDict)
        
        memo = {}
        res = []
        self.dfs(s, wordDict, memo, res) #dfs里唯一的变量是s->唯一确定一个memo
        return res
    
    def dfs(self, remaining, wordDict, memo, res):
        if remaining in memo: return memo[remaining]
        if remaining in wordDict:
            res.append(remaining)
        
        tmp = [] # level result
        for i in range(len(remaining)):
            left = remaining[:i]
            right = remaining[i:]
            if left in wordDict:
                next = self.dfs(right, wordDict, memo, res)
                for item in next:
                    tmp.append(left+" " + item)
                memo[remaining] = tmp 
        return memo[remaining]