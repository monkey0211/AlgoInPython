class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in "+-*/" or i == len(s) - 1: #最后一个数 既要参与上面if计算 也要在这里计算. 所以不能用elif
                if sign == "+":
                    stack.append(num)
                if sign == "-":
                    stack.append(-num)
                if sign == "*":
                    stack.append(stack.pop()*num)
                if sign == "/":
                    stack.append(int(stack.pop()/num)) # "//"不能做负数运算 需要用int(a/b)
                
                sign = c
                num = 0
        return sum(stack)