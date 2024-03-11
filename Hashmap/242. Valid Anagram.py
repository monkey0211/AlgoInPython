class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        # 先看长度是否相同
        # 题目要求using all the original letters exactly once-> 可用counter
        if len(s) != len(t): return False
        for char in s:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        
        for c in t:
            if c not in dict:
                return False
            else:
                dict[c] -= 1
        
        for k in dict.values():
            if k != 0:
                return False
        return True