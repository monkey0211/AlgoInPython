class Solution:
    # time O(2^n) 每次选和不选两个选择 一共left+right种. space: o(n) 栈的深度
    # dfs暴力枚举所有char, 每次尝试remove一个left or right, 直到遇到第一个valid就退出
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        # count how many left + right are un-matched(need to remove) in a string. 剩下没match上的 就是需要remove的
        left, right = self.lrRemovalCount(s)
        self.dfs(left, right, s, res, 0)
        return res
    
    def dfs(self, left, right, remaining, res, start):
        if left == 0 and right == 0:
            l, r = self.lrRemovalCount(remaining)
            if l == 0 and r == 0:
                res.append(remaining)
                return

        for i in range(start, len(remaining)):
            # 如果有重复就skip
            if i > start and remaining[i] == remaining[i-1]:
                continue
            
            if left > 0 and remaining[i] == "(": # Delete s[i]
                self.dfs(left - 1, right, remaining[:i]+ remaining[i+1:], res, i)
            elif right > 0 and remaining[i] == ")":  # Delete s[i]
                self.dfs(left, right - 1, remaining[:i]+ remaining[i+1:], res, i)
    
    def lrRemovalCount(self, s):
        l, r = 0, 0
        for char in s:
            if char == "(":
                l += 1
            elif char == ")":
                if l == 0:
                    r += 1
                else:
                    l -= 1
        return l, r
    
    #左括号数量需要一直比右括号多 否则return False
   


        