# job description distance:
# find the smallest distance between two words in a sentence

import collections


class Solution:
    def __init__(self, wordList):
        self.wordList = wordList
        self.wordIndexDict = collections.defaultdict(list)
        for i in range(len(wordList)):
            self.wordIndexDict[wordList[i]].append(i)
    
    def wordDistanceFinder(self, word1, word2):
        minDist = float("inf")
        if not word1 or not word2: return minDist
        
        word1Indices = self.wordIndexDict[word1] #[ 1,3]
        word2Indices = self.wordIndexDict[word2] #[2,4,5]
        
        i, j = 0, 0
        while i <= len(word1Indices) - 1 and j <= len(word2Indices)-1:
            minDist = min(minDist, abs(word1Indices[i] - word2Indices[j]))
            if word1Indices[i] < word2Indices[j]: #小的向后走
                i += 1
            else:
                j += 1
        return minDist

wordList = ["the", "quick", "brown","fox","quick"]
test = Solution(wordList)


print(test.wordDistanceFinder("fox", "the"))
print(test.wordDistanceFinder("quick", "fox"))

# TODO: follow up: if three words, how? sliding window