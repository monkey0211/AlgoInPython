class Solution:
    # # 有加减乘除 无括号
    # method 1: 不用stack: time O(n) space O(1)
    # 1. 如果ch.isdigit() 记录number
    # 2. 如果当前ch in "+-/*", 看previous sign(op): currTotal此时累进计算前面的+-*/
        # 2.1 如果当前ch in "+-", 把currTotal累加到总total, currTotal归零
        # 2.2 op = ch(把当前ch给op, 用op记录previous operator), num归零

    def calculate(self, s: str) -> int:
        currTotal = 0
        total = 0
        num = 0
        op = "+"  # keep the last operator we have seen
        
        # append a "+" sign at the end because we can catch the very last item
        for ch in s + "+":
            if ch.isdigit():
                num = 10 * num + int(ch)

            # 遇到符号 计算之前的部分calculate the previous part.
            # note that we have to catch the last chracter since there will no sign afterwards to trigger calculation
            if ch in ("+", "-", "*", "/"):
                if op == "+":
                    currTotal += num
                elif op == "-":
                    currTotal -= num
                elif op == "*":
                    currTotal *= num
                elif op == "/":
                    # in python if there is a negative number, we should alway use int() instead of //
                    currTotal = int(currTotal / num)
                
                # 如果是“+-” 总结前一步的: add currTotal to total and reset currTotal
                if ch in ("+", "-"):
                    total += currTotal
                    currTotal = 0
                
                op = ch #把当前ch给op, 用op记录previous operator
                num = 0
        
        return total
    # method 2: stack time O(n) space O(n)
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