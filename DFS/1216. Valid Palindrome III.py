class Solution:
   # DFS + memo: dfs表示: s[i:j] at current level, is valid palindrome T/F if removing k
   # memo记住状态memo[(i, j, k)]
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = {} 
        return self.dfs(0, len(s) - 1, s, k, memo)

    def dfs(self, i, j, s, count, memo):
        # at current level, if this is valid palimdrome if removing k
        if count < 0:
            return False
        if i >= j:
            return True
        
        if (i, j, count) in memo: 
            return memo[(i, j, count)]
        
        if s[i] == s[j]: # 如果左右char相等
            res = self.dfs(i + 1, j - 1, s, count, memo) #i,j meet, so still have k budget
        else:
            res = self.dfs(i+1, j, s, count - 1, memo) or self.dfs(i, j-1, s, count-1, memo)
        memo[(i, j, count)] = res # res is boolean T/F
        return res
