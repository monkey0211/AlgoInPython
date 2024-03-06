class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # time o(n), space o(n)
        # 要点: 1. 对每一个字母 如果之前有比他小的出现 他就应该排在后面出现. (所以需要记录每一个字母最后一次出现的位置lastOcurrence)
        # 2. 
        lastOccurrence = {}
        seen = set()
        # 1. 记录每一个字母最后一次出现的位置lastOccurrence[c] = i
        for i, c in enumerate(s):
            lastOccurrence[c] = i
          
        # 2. 如果当前char比之前小, 需要看stack[-1]是否后面还会出现, 如果有就pop(), 等后面出现再放入
        stack = []
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and lastOccurrence[stack[-1]] > i:
                    seen.discard(stack.pop()) # python set.discard(): to removel from set, and if not exist won't raise exception.
                seen.add(c)
                stack.append(c)
        
        return "".join(stack)