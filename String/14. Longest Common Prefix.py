'''
以第一个str为基准 扫描剩下n-1个str
时间O(S), where S is the total number of chars. 空间O(1)

如果query非常多怎么办? -> 把strs建成trie
'''
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])): # 最长前缀不会超过strs[0]的长度
            char = strs[0][i] # 取出第i个字符
            for j in range(1, len(strs)): # 遍历剩下字符串j的每一个字符
                if i == len(strs[j]) or strs[j][i] != char: # 第j个字符走到头 或者 第i个字符与strs[j][i]不匹配
                    return strs[0][:i] # [:i]左闭右开
        return strs[0]