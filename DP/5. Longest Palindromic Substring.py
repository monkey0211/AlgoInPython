class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 马拉车算法(一种dp)
        # 以每个元素为中心 可以向两边扩展
        # p[i]: the longest extended radius palindromic substrings centered at i
        if not s: return ""
        res = ""
        for i in range(len(s)):
            p1 = self.palindrome(s, i, i+1)
            p2 = self.palindrome(s, i, i)
            if len(p1)>len(res): #每次p1, p2和current result比较, 不是len(p1)&len(p2)比较, 否则res is the latest updated p1/p2
                res = p1
            if len(p2)>len(res):
                res = p2
            
        return res
    
    def palindrome(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        return s[left + 1: right]
        