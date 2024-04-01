class Solution:
    def countSubstrings(self, s: str) -> int:
        # similar to LC5: 从一个center出发向两边扩展, 此题只需要计算个数即可
        # p[i]: the longest extended radius palindromic substrings centered at i
        # 单个自负需要算在内, 因为center本身就是
        if not s: return 0
        res = 0
        for i in range(len(s)):
            p1 = self.palindrome(s, i, i + 1)
            p2 = self.palindrome(s, i, i)
            res += p1+p2
        return res
        
    def palindrome(self, s, left, right):
        res = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
            else:
                break #need to break
        return res