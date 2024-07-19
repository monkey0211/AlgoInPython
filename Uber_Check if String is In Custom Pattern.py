#time o(n)
class Solution: 
    def checkPattern(self, s, pattern): 
        
        # track the label (or order) of last visited character
        index = {}
        for i in range(len(s)):
            index[s[i]] = i

        lastIndex = -1
        # Give the pattern characters order
        for i in range(len(pattern)):
            if pattern[i] in s:
                if lastIndex == -1:
                    lastIndex = index[pattern[i]] #先找上一个的index
                    continue
                else:
                    currIndex = index[pattern[i]] 
                if currIndex < lastIndex:
                    return False
                lastIndex = currIndex
                
        return True
        
                
test = Solution()
s = "engineers rock"     
pattern = "gsr"
print(test.checkPattern(s, pattern))