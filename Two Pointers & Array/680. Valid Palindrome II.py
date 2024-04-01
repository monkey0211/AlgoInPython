class Solution:
    # two pointer: 
    def validPalindrome(self, s: str) -> bool:
        if not s: return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(left + 1, right, s) or self.isPalindrome(left, right - 1, s)           
            else:
                left += 1
                right -= 1
        return True
    
    def isPalindrome(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        