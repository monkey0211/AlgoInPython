class Solution:
# method1: stack. time o(n) space o(n)
# - 建立一个removal set记录需要remove的index(因为不能边遍历边remove)
# - 建立stack 存所有的左括号, 如果遇到右括号: 如果无stack 加入removal. else直接带走左括号
# - stack里最后剩余所有的“(” 都是多余的 加入removal
# - 最后返回除了removal的剩余string
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        removal = set()
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if not stack: #没有左括号 说明有多余的右括号 把index加入removal set 
                    removal.add(i)          
                else:
                    stack.pop()
        # 最后stack里如果还有剩余 就是都需要去掉的左括号
        while stack:
            removal.add(stack.pop())
        for i in range(len(s)):
            if i not in removal:
                res += s[i]
        return res
    
    # method 2: 不用stack直接计算open and balance括号个数
    def minRemoveToMakeValid(self, s: str) -> str:
        # Pass 1: Remove all invalid ")"
        first_pass_chars = []
        balance = 0
        open_seen = 0
        for c in s:
            if c == "(":
                balance += 1
                open_seen += 1
            if c == ")":
                if balance == 0:
                    continue  #ignore剩下的左括号
                balance -= 1
            first_pass_chars.append(c)

        # Pass 2: Remove the rightmost "("
        result = []
        open_to_keep = open_seen - balance #计算应该保留的右括号个数
        for c in first_pass_chars:
            if c == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue #ignore剩下的右括号
            result.append(c)

        return "".join(result)
        
        