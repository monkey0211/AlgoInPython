class Solution:
    # two pointer 先看abbr. 遇到数字用 isdigit(), 用tmp记录数字部分 然后用int()可以拿到. 
    # 注意最后需要return i==len(word) and j == len(abbr) 确保两个都遍历完.
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not word or len(word) < len(abbr): return False

        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i]!=abbr[j]:
                if abbr[j] == "0":
                    return False
                    break
                if abbr[j].isdigit():
                    tmp = ""
                    length = 0
                    while j < len(abbr) and abbr[j].isdigit():
                        tmp += abbr[j]                    
                        j += 1
                i += int(tmp) #直接用int()可以转换
            else:  
                i += 1
                j += 1
        return i == len(word) and j == len(abbr) #不能直接return True. 如果两个单词最后长度不同 还有剩余一个没有遍历完.
        