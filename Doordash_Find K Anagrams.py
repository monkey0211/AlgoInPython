import collections

class Solutions:
# doordash Q2: https://leetcode.com/discuss/interview-question/1505566/doordash-coding-new-grad

# Given a restaurant name, find other restaurants in the list that are k-anagrams with each other. A name is a k-anagram with another name if both the conditions below are true:
# The names contain the same number of characters.
# The names can be turned into anagrams by changing at most k characters in the string
# For example:
# name = "grammar", k = 3, and list = ["anagram"], "grammar" is k-anagram with "anagram" since they contain the same number of characters and you can change 'r' to 'n' and 'm' to 'a'.
# name = "omega grill", k = 2 and list = ["jmegra frill"], "omega grill" is k-anagram with "jmega frill" since they contain same number of characters and you can change 'o' to 'j' and 'g' to 'f'

# 1.Check if length of string is the same
# 2.Build out counterTarget
# 3.for char in sourceString, count the total number of differences. add to res if <=K
    def findKAnagrams(self, name, list, K):
        res = set()
        for n in list:
            if len(n) == len(name):
                counterN = collections.Counter(n)
                diff = self.getMinDiff(name, n, counterN)   
                if diff <= K: 
                    res.add(n)
        return res
    def getMinDiff(self, s, n, counterN):
        diff = 0
        for char in s:
            if char not in counterN:
                diff += 1
            else:
                if counterN[char] > 0:
                    counterN[char] -= 1
                else:
                    diff += 1
        return diff
        

test = Solutions()
name = "grammar"
list = ["anagram"]
K = 3
print(test.findKAnagrams(name, list, K))

# followup: 如果input过长，用mapreduce的思路怎么解决