class Solution:
    # Time O(max(m,n))
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ""
        # or的关系, 如果位数不够补零
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            sum = a + b + carry
            carry = sum // 10
            i -= 1
            j -= 1
            res = str(sum % 10) + res #新的digit要加在res之前一位 
        
        if carry == 1:
            res = "1" + res
        return res

