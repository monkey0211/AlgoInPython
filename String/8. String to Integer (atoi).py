class Solution:
    def myAtoi(self, s: str) -> int: 
        s = s.strip()
        if not s: return 0 #必须放在截断之后
        sign = 1
        res = 0
        maxInt = 2**31 - 1
        minInt = -2**31
        
        start = 0
        if s[0] == "-":
            sign = -1
            start += 1
        elif s[0] == "+":
            start += 1
        for i in range(start, len(s)):
            if not s[i].isdigit():
                break
            
            res = res*10 + int(s[i]) #包括首位0的情况: 如果首位是0,res=0
            print(res)
        res = res*sign
        if res < minInt: 
            return minInt
        if res > maxInt:
            return maxInt
        return res
        