class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        res = 0
        while x > 0:
            x, remainder = x // 10, x % 10
            res = res * 10 + remainder 
        res *= sign
        if res < - 2**31 or res >= 2**31 - 1:
            return 0
        return res
