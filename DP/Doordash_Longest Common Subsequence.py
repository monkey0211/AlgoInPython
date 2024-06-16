# Doordash版本: LC变种 https://leetcode.com/problems/longest-common-subsequence/description/
# 需要打印所有路径 不只是maxValue
class Solution:
    #use i, j as text1 and text2 pointers
    #use DFS to find the the longest common subsequence for text1[i:] and text2[j:]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}
        return self.dfs(0, 0, text1, text2, memo)
    
    def dfs(self, i, j, text1, text2, memo):
        if (i, j) in memo: return memo[(i, j)]
        if i == len(text1) or j == len(text2):
            return {""}
        
        res = set()
        if text1[i] == text2[j]:
            sub_res = self.dfs(i + 1, j + 1, text1, text2, memo)
            res = {text1[i] + char for char in sub_res}
        else:
            sub_res_text1 = self.dfs(i + 1, j, text1, text2, memo)
            sub_res_text2 = self.dfs(i, j + 1, text1, text2, memo)
            
            max_len_sub_1, max_len_sub_2 = -1, -1
            for item in sub_res_text1:
                max_len_sub_1 = max(len(item), max_len_sub_1)
            for item in sub_res_text2:
                max_len_sub_2 = max(len(item), max_len_sub_2)
            
            if max_len_sub_1 > max_len_sub_2:
                res = sub_res_text1
            elif max_len_sub_2 > max_len_sub_1:
                res = sub_res_text2
            else:
                res = sub_res_text1 | sub_res_text2
        memo[(i, j)] = res
        return res


text1 = "abc"
text2 = "abc" 
test = Solution()
print(test.longestCommonSubsequence(text1, text2))