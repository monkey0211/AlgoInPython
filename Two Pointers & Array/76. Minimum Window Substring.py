class Solution:
# ts O(S+T). sc O(S+T)
# 在string s里找到包含string t的最短s(s可以不连续)
# counterT固定，counterS不断更新
# for左指针， 动右指针j，不满足条件就向右。
# 跳出while之后更新min, 然后counterS去掉左指针
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        counterT = collections.defaultdict(int)
        for ch in t:
            counterT[ch] += 1
        counterS = collections.defaultdict(int)
        j = 0
        minLen = inf

        res = ""
        for i in range(len(s)):
            while j < len(s) and not self.isValid(counterT, counterS):
                #右端点前进一个 counterS +1
                counterS[s[j]] += 1
                j += 1
            if self.isValid(counterT, counterS) and j-i < minLen:
                minLen = j-i
                res = s[i:j]
            # i左端点前进一个 counterS需要减少
            counterS[s[i]] -= 1
        return res
    
    def isValid(self, counterT, counterS):
        # check if counterS contains everything in counterT
        for key in counterT:
            if key not in counterS:
                return False
            else:
                if counterS[key] < counterT[key]:
                    return False
        return True

    # Aaron version: 优化了上面isValid()中 对两个counter遍历检查的时间复杂度
    # j是左窗口 i是右窗口 当hs(hashtable s)中 s[j]字符出现的次数 大于ht时 移动左窗口j 并更新hs
    def minWindow(self, s: str, t: str) -> str:
        hs, ht = Counter(), Counter(t)
        res, count = "", 0
        j = 0
        for i in range(len(s)):
            hs[s[i]] += 1
            if hs[s[i]] <= ht[s[i]]:
                count += 1
            while j < len(s) and hs[s[j]] > ht[s[j]]:     
                hs[s[j]] -= 1
                j += 1
            if count == len(t): # 找到一个满足条件的窗口 判断是否更新答案
                if not res or i - j + 1 < len(res):
                    res = s[j: i+1]
        return res