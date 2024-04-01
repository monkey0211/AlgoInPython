    # https://www.youtube.com/watch?v=JqOIRBC0_9c 
    # 此题需要记录all possible results. LC139只需要返回True/False
    # 需要memo:
    # memo一般都是用来记录最终结果, 在dfs里代表记录每个需要分隔的remaining的all possible result list(结果)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = defaultdict(list) 
        
        return self.dfs(s, wordDict, memo)
        #or: return memo[s]
    
    def dfs(self, remaining: str, wordDict: set[str], memo: dict[str: List[str]]):
        if remaining in memo:
            return memo[remaining]
        #tmp是记录每次切分的result. eg ["cats and", "cat sand"]
        tmp = []
        if remaining in wordDict:
          tmp.append(remaining)

        #拆分成左右两部分: inDict(left) + dfs(right)
        for i in range(len(remaining)):
            left = remaining[:i]
            right = remaining[i:]
         
            if left in wordDict:
                nxt = self.dfs(right, wordDict, memo)
                # 把拿到的结果拼接: dict[cats] + ["and dog", "an ddog", "a nddog"]
                # 需要在if里面进行
                for item in nxt:
                    tmp.append(left + " " + item)
        #put result into memo. 
        memo[remaining] = tmp
        return memo[remaining]