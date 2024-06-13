import collections

class Solutions:
# doordash: https://leetcode.com/discuss/interview-question/1505566/doordash-coding-new-grad

# Q1: Two restaurants R1 and R2 are similar if we can swap a maximum of two letters (in different positions) of R1, so that it equals R2.      
# 1.Check if length of string is the same
# 2.Check if they contain the same character frequency
# 3.Have two pointer go through the two strings, respectively. There can be at most 2 character mismatches.
    def findSimilarRestaurants(self, name, list, K):
        counterName = collections.Counter(name)
        res = set()
        for n in list:
            counterN = collections.Counter(n)
            if len(n) == len(name) and counterN == counterName:
                if self.isValidKAnagram(name, n, K):
                    res.add(n)
        return res
    
    def isValidKAnagram(self, name, n, K):
        i = 0
        diff = 0
        while i < len(n):
            if n[i] != name[i]:
                diff += 1
                if diff > K:
                    return False
            i += 1
    
        return True

# test = Solutions()
# input = "hotpot"
# list = ["hottop", "hotopt", "hotpit", "httoop", "hptoot"]
# # print(["hottop", "hotopt", "hptoot"])

# input = "biryani"
# list = ["biryani", "biryeni", "biriyani", "biriany", "briynai"]
# # print(["biryani", "biriany"])

# print(test.findSimilarRestaurants(input, list, 2))          

        
# Q2:
# Given a restaurant name, find other restaurants in the list that are k-anagrams with each other. A name is a k-anagram with another name if both the conditions below are true:
# The names contain the same number of characters.
# The names can be turned into anagrams by changing at most k characters in the string
# For example:
# name = "grammar", k = 3, and list = ["anagram"], "grammar" is k-anagram with "anagram" since they contain the same number of characters and you can change 'r' to 'n' and 'm' to 'a'.
# name = "omega grill", k = 2 and list = ["jmegra frill"], "omega grill" is k-anagram with "jmega frill" since they contain same number of characters and you can change 'o' to 'j' and 'g' to 'f'

# 1.Check if length of string is the same
# 2.Build out their counter table
# 3.Go through both counter table, count the total number of differences. True if within k, false if not.
    def findKAnagrams(self, name, list, K):
        res = set()
        counterName = collections.Counter(name)
        for n in list:
            if len(n) != len(name):
                return res
            counterN = collections.Counter(n)
            diff = 0
            for char in counterN:
                diff += abs(counterN[char] - counterName[char])
            if diff/2 <= K: #because we count twice for both directions(if can switch)
                res.add(n)
        return res

# test = Solutions()

# input = "omexyb grillg"
# list = ["omgxca grille"]
# K = 2
# print(test.findKAnagrams(input, list, K))
