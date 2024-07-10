class Solution:
    # 数学方法直接看original==reversed
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        original = x #need to save x value.
        reversed = 0
        while x > 0:
            remainder = x % 10
            reversed = reversed*10 + remainder
            x = x // 10
     
        return original == reversed
            
        