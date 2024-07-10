class Solution:
    # 有加减和括号
    def calculate(self, s: str) -> int:
        num = 0
        res = 0
        sign = 1
        stack = []
        for ch in s:
            if ch.isdigit():
                num = 10*num + int(ch)
            elif ch == "+":
                res += sign*num
                num = 0
                sign = 1 #把现在的sign交给下一次
            elif ch == "-":
                res += sign*num
                num = 0
                sign = -1
            elif ch == "(":
                stack.append(res) #需要append previous res(不是num)&sign, then reset
                stack.append(sign)
                sign = 1 #交出去给stack之后需要重置
                res = 0
            elif ch == ")":
                res += sign*num #结算当前括号里的结果(同+-时候的情况)
                res *= stack.pop() #pop previous sign
                res += stack.pop() #pop previous res
                num = 0
                sign = 1
        if num != 0: #最后还有一位没有结算
            res += sign * num
        return res

        