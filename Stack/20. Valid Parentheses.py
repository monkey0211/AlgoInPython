class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if not stack: return False # corner case: s = "]" so no stack at this time.
                if (c == ")" and stack[-1] == "(") or (c == "]" and stack[-1] == "[") or (c == "}" and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
        if not stack: return True
        return False