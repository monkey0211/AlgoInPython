'''
思路: 
The idea is to add ')' only after valid '('
We use two integer variables left & right to see how many '(' & ')' are in the current string
 - If left < n then we can add '(' to the current string
 - If right < left then we can add ')' to the current string

时间O(4^n / (n*sqrt(n))) -> in the order of exponential
空间O(n)
'''
from typing import List

class Solution:
    # 方法1: DFS
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        self.dfs(0, 0, '', n, ret)
        return ret
    
    def dfs(self, left, right, s, n, ret):
        if len(s) == n * 2:
            ret.append(s)
            return
        if left < n:
            self.dfs(left + 1, right, s + '(', n, ret)

        if right < left:
            self.dfs(left, right + 1, s + ')', n, ret)

    # 方法2: iterative
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        left = right = 0
        q = [(left, right, '')]
        while q:
            left, right, s = q.pop()
            if len(s) == 2 * n:
                result.append(s)
            if left < n:
                q.append((left + 1, right, s + '('))
            if right < left:
                q.append((left, right + 1, s + ')'))
        return result