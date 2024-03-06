class Solution:
# 从前到后遍历即可, 分别两个变量记录净open和净close个数(反向open)
# 不能合并 需要考虑有“))((”情况
# 最后return open+close
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        close = 0
        for c in s:
            if c == "(":
                open += 1
            elif c == ")":
                open -= 1
                if open < 0:
                    close += 1
               
      
        return open + close
        