class Solution:
    #return all possible-> DFS, combination
    def partition(self, s: str) -> List[List[str]]:
        if not s: return []
        res = []
        tmp = []
        self.dfs(res, tmp, 0, s)
        return res
    #dfs: 每切一个位置, 如果前半部分是palindrome, 用递归dfs看后半部分
    def dfs(self, res, tmp, index, s):
        #recursion结束: 前半部分全部都是palindrome, 无remainder
        if len(s[index:]) == 0:
            res.append(tmp[:])
            return
        for i in range(index, len(s)):
            prefix = s[index:i+1] #prefix从s[index]开始
            if self.isPalindrome(prefix):
                tmp.append(prefix)
                self.dfs(res, tmp, i+1, s)
                tmp.pop()
    def isPalindrome(self, s):
        return s == s[::-1]
