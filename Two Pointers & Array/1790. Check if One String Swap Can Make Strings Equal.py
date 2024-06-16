class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if not s1 or not s2: return False
        if len(s1)!= len(s2): return False

        res = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                res.append(i)
        if len(res) > 2: return False
        return len(res) == 0 or (len(res) == 2 and s1[res[0]] == s2[res[1]] and s1[res[1]] == s2[res[0]])
        