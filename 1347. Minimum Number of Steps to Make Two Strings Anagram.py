class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counterT = collections.Counter(t)
        diff = 0
        for char in s:
            if char not in counterT:
                diff += 1
            else:
                if counterT[char] > 0:
                    counterT[char] -= 1
                else:
                    diff += 1
        return diff
        