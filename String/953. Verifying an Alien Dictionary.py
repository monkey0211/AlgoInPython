class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(min(len(word1), len(word2))):
                if word1[j]!=word2[j]:
                    if order.index(word1[j]) > order.index(word2[j]):
                        return False
                    break #注意break的位置 不能在内层if里, 因为只要字母不相等 任何情况都需要break
                else:
                    #剩余的情况 如果len(word1)>len(word2)
                    if  len(word1) > len(word2) and j == len(word2) - 1:
                        return False
        return True
            
        