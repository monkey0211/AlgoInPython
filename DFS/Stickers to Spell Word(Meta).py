# Meta version:(ref LC691) https://leetcode.com/discuss/interview-question/4835013/Meta-Minimum-Stickers-Required


# Problem Description:
# Given a string sticker that represents the set of characters available on a single sticker and a string word that represents the target word to spell out, 
# return the minimum number of stickers that you need to spell out word. 
# Each sticker can be used more than once, and you have an unlimited supply of stickers.

# public int minStickers(String sticker, String word) {
# }
# Example 1:
# Input: sticker = "ban", word = "banana"
# Output: 3
# Explanation: We can use 3 stickers "bana" to spell out the word "banana". Each sticker provides one "b", one "a", and one "n". Three stickers provide all the letters needed to spell out "banana".

# Example 2:
# Input: sticker = "abc", word = "def"
# Output: -1
# Explanation: The sticker does not contain any of the letters needed to spell out "def". Therefore, it is impossible to spell out the word.

# Constraints:
# 1 <= sticker.length, word.length <= 1000
# sticker and word consist of lowercase English letters.
import collections
from math import inf
class Solution: 
    def countMinStickers(sticker: str, word: str) -> int:
        counterS = collections.Counter(sticker)
        counterW = collections.Counter(word)
			
        minCnt = inf
        for c in word:
            if c not in counterS:
                return -1
            else:
                cnt = math.ceil(counterS[c]/counterW[c]) #取upper值
                minCnt = max(minCnt, cnt) #注意是Max
        return minCnt


# print(countMinStickers("ban", "banana")) => 3
# print(countMinStickers("abc", "def")) => -1
# print(countMinStickers("banaan", "banana")) => 1