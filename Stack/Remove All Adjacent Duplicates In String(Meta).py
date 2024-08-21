# ref 1047: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# 给出string, 需要你去除重复的相连的字母
# 如 "abbba" -> "aa" -> ""
# "ab" -> "ab"
'''
It uses an index to track where to place non-duplicate characters. 
It skips over duplicate characters and moves only unique characters forward. 
After processing the original string, trims the original string to remove extra characters. 

If any adjacent duplicates were removed in this process then recursively call the function itself 
to repeat this process again. 

This approach is efficient because it modifies the string directly without creating new ones.
'''
# Helper function to remove adjacent duplicates
def remove_util(s, n):
    # Index to store the result string
    k = 0
    # Iterate over the string to remove adjacent
    # duplicates
    i = 0
    while i < n:
        # Check if the current character is the
        # same as the next one
        if i < n - 1 and s[i] == s[i + 1]:
            # Skip all the adjacent duplicates
            while i < n - 1 and s[i] == s[i + 1]:
                i += 1
        else:
            # If not a duplicate, store the character
            s[k] = s[i]
            k += 1
        i += 1
    # Remove the remaining characters from
    # the original string
    s = s[:k]
    # If any adjacent duplicates were removed,
    # recursively check for more
    if k != n:
        s = remove_util(list(s), k)
    return s
# Function to initiate the removal of adjacent duplicates
def rremove(s):
    # Convert the string to a list to allow modification
    s = list(s)
    # Call the helper function
    return ''.join(remove_util(s, len(s)))

# Example usage
s = "abbbaca"
print(rremove(s))


# 下面这个实现有些问题 先不要看
'''
# 用stack 但是需要特别处理while stack pop之后最后一个元素(也需要抹去)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ""
        prev = ""
        stack = []
        for ch in s:
            if not stack and ch != prev:
                stack.append(ch)
            else:
                while stack and stack[-1] == ch:
                    prev = stack.pop()
                stack.append(ch)
                if ch == prev:
                    stack.pop()
        print(stack)
        return "".join(stack)
'''

        