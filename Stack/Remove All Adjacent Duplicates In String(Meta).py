# ref 1047: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# 给出string, 需要你去除重复的相连的字母
# 如 "abbba" -> "aa" -> ""
# "ab" -> "ab"

# 用stack 但是需要特别处理while stack pop之后最后一个元素(也需要抹去)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ""
        prev = ""
        stack = []
        for ch in s:
            if not stack and ch != prev:
                stack.append(ch)
            else:
                while stack and stack[-1] == ch:
                    prev = stack.pop()
                stack.append(ch)
                if ch == prev:
                    stack.pop()
        print(stack)
        return "".join(stack)

        