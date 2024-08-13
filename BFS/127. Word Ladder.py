class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        queue = collections.deque([beginWord])
        wordSet = set(wordList)

        cnt = 0
        while queue:
            cnt += 1
            for i in range(len(queue)):
                word = queue.popleft()
                visited.add(word)
                if word == endWord:
                    return cnt
                
                for nextword in self.searchNextWord(word, wordSet):
                    if nextword not in visited:
                        queue.append(nextword)
                        visited.add(nextword)
        return 0
    
    def searchNextWord(self, word, wordSet):
        words = []
        for i in range(len(word)):
            for j in "abcdefghijklmnopqrstuvwxyz":
                newword = word[:i] + j + word[i+1:]
                if i != j and newword in wordSet:
                    words.append(newword)
        return words

# Linkedin Followup
# 1. what change to make if this has to become an online service? how will you minimize latency?
# pre-compute the pairs and store the paths. use all pair shorted path along with modifications to store the paths. 
# handle updates to dictionaries. 