class Solution:
    # stack里放入tuple(char, cnt) cnt == k时都pop掉. 不会出现cnt > k的情况
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res = []
        for c in s:
            if not stack or c != stack[-1][0]:
                stack.append((c, 1))
            else:
                if stack[-1][0] == c and stack[-1][1] < k:
                    stack.append((c, stack[-1][1]+1))
                    if stack[-1][1] == k:
                        while stack and stack[-1][0] == c and stack[-1][1] > 0: # 需要注意while stack问题
                            stack.pop()         
        
        while stack:
            res.append(stack.pop()[0])
        return "".join(reversed(res))
