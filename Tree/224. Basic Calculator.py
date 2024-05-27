class Solutions:
    def calculate(self, s: str) -> int:
        
#         num = 0
#         res = 0
#         sign = 1
#         stack = []
#         for c in s:
#             if c.isdigit():
#                 num = 10*num + int(c)
#             elif c == "+":
#                 res += sign*num
#                 num = 0      #重置num
#                 sign = 1     #把现在的sign交给下一次
#             elif c == "-":
#                 res += sign*num
#                 num = 0      #重置num
#                 sign = -1    #把现在的sign交给下一次
#             elif c == "(":    #需要append previous res(不是num)&sign, then reset
#                 stack.append(res)
#                 stack.append(sign)
#                 sign = 1       #交出去给stack之后需要重置
#                 res = 0
#             elif c == ")":
#                 res += sign*num      #结算当前括号里的结果(同+-时候的情况)
#                 res *= stack.pop()      #pop previous sign
#                 res += stack.pop()      #pop previous res
#                 num = 0
#                 sign = 1 #是否重置都可以 因为此时num = 0

#         if num != 0:         #最后还有一位没有结算
#             res += sign * num
#         return res