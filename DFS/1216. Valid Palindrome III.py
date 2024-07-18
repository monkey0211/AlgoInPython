class Solution:
   # dfs表示s[i:j]最多remove多少个可以变成palindrome
   # time o(n^2) space o(n^2) n is length of string. (because i*j个组合memo)
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = {}
        return self.dfs(0, len(s) - 1, s, memo) <= k

    def dfs(self, i, j, s, memo) -> bool:
       
        if i == j:         # i and j meet
            return 0

        #  Base case 2, only 2 letters remaining.
        if i == j - 1:
            return 1 if s[i] != s[j] else 0

        if (i, j) in memo:  # (i, j, count) is a searched state
            return memo[(i, j)]
        
        ret = 0
        if s[i] == s[j]:
            ret = self.dfs(i + 1, j - 1, s, memo)
        else:
            ret = 1 + min(self.dfs(i + 1, j, s, memo), self.dfs(i, j - 1, s, memo))
        memo[(i, j)] = ret  # keep track of bool result of current state
        
        return ret