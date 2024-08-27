import collections
from typing import List
class Solution:
    # method 1: BFS直接遍历26个字母找neighbor as nextWord
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

    # method2: BFS build graph. graph可以提前build好, 所以适用于service的情况
    # 
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        # 把开始词也需要放入word_list
        if begin_word not in word_list:
            word_list.append(begin_word)
            
        # 1.构建patterns: 每个word_list里面的每个字母都替换为*
        # *ot: {"hot", "dot", "lot"}
        # h*t: {"hot"}
        # ho*: {"hot"}
        # d*t: {"dot"}
        # do*: {"dot", "dog"}
        patterns = collections.defaultdict(set)
        for word in word_list:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                patterns[key].add(word)
    
        # 2. Create a graph between words using patterns
        # "hit": ["hot"] （通过 h*t 找到）
        # "hot": ["dot", "lot", "hit"] （通过 *ot, h*t, ho* 找到）
        graph = collections.defaultdict(set)
        for word in word_list:
            neighborSet = set()
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                neighborSet |= patterns[key] #取并集union two sets
 
            graph[word] = neighborSet
   
        # find the shortest way between begin_word and end_word
        # -> BFS
        queue = collections.deque([begin_word])
        step = 0
        visited = set([begin_word])
        while queue:
            step += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == end_word:
                    return step
                for next_word in graph[word]:
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append(next_word)
        return 0

# implement as a service, 可以用try exception. eg:
# try:
#     num1 = int(input("Enter 1st number:"))
#     num2 = int(input("Enter 2nd number:"))
# except ValueError as ve:
#     print(ve)
#     rollbar.report_exc_info()
#     exit()