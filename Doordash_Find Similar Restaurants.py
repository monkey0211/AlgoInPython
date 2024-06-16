import collections

class Solutions:
# doordash: https://leetcode.com/discuss/interview-question/1505566/doordash-coding-new-grad
# ref: LC859 https://leetcode.com/problems/buddy-strings/description/
# Q1: Two restaurants R1 and R2 are similar if we can swap a maximum of two letters (in different positions) of R1, so that it equals R2.      
# 1.Check if length of string is the same
# 2.Check if they contain the same character frequency
# 3.Check if buddy strings.1)s == name, if counter has twice items->True. 2) general case: 看diff
    def findSimilarRestaurants(self, s, list):
        counterS = collections.Counter(s)
        res = set()
        for n in list:
            counterN = collections.Counter(n)
            if len(n) == len(s) and counterN == counterS:
                if self.isValidBuddyString(s, n, counterS):
                    res.add(n)
        return res
    
    def isValidBuddyString(self, s, n, counterS):
        # 1) 如果s == n 如果有任何一个char重复两次以上 就一定可以switch -> True
        if s == n:
            for char in counterS:
                if counterS[char] >= 2:
                    return True
        
         # general情况: 逐个比较两个char 如果有不同就记录index, 
         # 最后return两个s[indexList[0]] == goal[indexList[1]] 是否相等 

        res = []
        for i in range(len(s)):
            if s[i] != n[i]:
                res.append(i)
            if len(res) > 2:
                return False
        return len(res) == 2 and s[res[0]] == n[res[1]] and s[res[1]] == n[res[0]]

test = Solutions()
input = "hotpot"
list = ["hottop", "hotopt", "hotpit", "httoop", "hptoot"]
# # print(["hottop", "hotopt", "hptoot"])

# input = "biryani"
# list = ["biryani", "biryeni", "biriyani", "biriany", "briynai"]
# # print(["biryani", "biriany"])

print(test.findSimilarRestaurants(input, list))          