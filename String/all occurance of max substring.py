'''
https://leetcode.com/company/facebook/discuss/5518268/Meta-Screening-(-July-2024-)
Given a string, find all the occurance of maximum length substring with repeating character 
and list in the order it appears.

Example : aaabbaaaccc , output => ['a','a','c'].
'''

# O(n) time complexity, single pass
# O(1) space as res is considered to be solution that is being returned

def maxLenRepeatingCharSubstrings(input):
    res = [] # to store char of substring that is of max len
    maxLen = 1
    
    p = 0
    while p<len(input):
        i = p
        # capture all substring with same chars
        while i+1<len(input) and input[i+1] == input[p]:
            i += 1
        
        # update maxLen and res
        length = i-p+1
        if length == maxLen:
            # if len is same as maxLen, append to res
            res.append(input[p])
        elif length > maxLen:
            # if found a new maxLen, reset res with new char
            res = [input[p]]
            maxLen = length
        
        # increment to next position (or substring)
        p = i+1
    
    return res

print(maxLenRepeatingCharSubstrings('aaabbaaaccc')) # Output: [a,a,c]
print(maxLenRepeatingCharSubstrings('bbaa')) # Output: [b,a]
print(maxLenRepeatingCharSubstrings('cbbaa')) # Output: [b,a]
print(maxLenRepeatingCharSubstrings('')) # Output: []
print(maxLenRepeatingCharSubstrings('a')) # Output: [a]
print(maxLenRepeatingCharSubstrings('ab')) # Output: [a,b]
print(maxLenRepeatingCharSubstrings('abcbca')) # Output: [a,b,c,b,c,a]