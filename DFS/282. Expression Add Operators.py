class Solution:   
    # 乘法时候需要计算preSum, 把前一个数减掉再加回
    # 1 2 3 4 5 --> 1 + 2 + 3 + 4 * 5
    #               ^ ^ ^ ^ ^ ^ ^ == 10 but we wanna do 4*5 so ---
    # just do 1 + 2 + 3 + 4 + (- 4) + (4 * 5)
    # return ans
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.dfs(res, num, target, 0, "", 0, 0)
        return res

    # i: 切分的startIndex, 后一半string的startIndex
    # tmp: string里已经处理过的前半部分
    # prev_add: 指的是现在的数 传给下一次total计算时候 作为下一次的prev_add
    # total: 现在的累计total
    def dfs(self, res, num, target, i, tmp, prev_add, total):
        if i == len(num) and total == target:
            res.append(tmp)
            return
        
        for j in range(i, len(num)):
            # starting with zero的数, 后面就可以不用继续了
            s = int(num[i:j + 1])
            if len(num[i:j+1]) > 1 and num[i] == "0": 
                break

            # if cur index is 0 then simple add that number
            if i == 0:
                self.dfs(res, num, target, j + 1, str(s), s, s)
            else:
                self.dfs(res, num, target, j + 1, tmp + "+" + str(s), s, total + s)
                self.dfs(res, num, target, j + 1, tmp + "-" + str(s), -s, total - s)
                self.dfs(res, num, target, j + 1, tmp + "*" + str(s), prev_add*s, total - prev_add + prev_add*s)
