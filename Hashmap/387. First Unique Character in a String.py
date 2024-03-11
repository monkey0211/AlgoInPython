class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        dict = collections.defaultdict(int)
        for char in s:
            dict[char] += 1
        
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1

        