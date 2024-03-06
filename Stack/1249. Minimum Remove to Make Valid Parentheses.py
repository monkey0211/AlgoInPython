class Solution:
# time o(n) space o(n)
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
        