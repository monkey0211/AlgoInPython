class Solution:
# 一行一行拿出来解析 每一行先看最后一个word是否超额, 如果超了算下一行. 最后一行需要单独计算
# 注意最后做line adjustment的时候 要计算每个空格能塞进去多少: spaces, extra = rest//total_space, rest % total_space
# **time O(n) space O(n) worst**
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = [] #words that are in current line.
        line_cnt = 0
        #len(line)代表空格个数
        for word in words:
            if line_cnt + len(word) + len(line) <= maxWidth:
                line += [word]
                line_cnt += len(word)
            else: #if line is full
                modline = self.formatLine(line, line_cnt, maxWidth)
                res += [modline]
                line = [word] #this is first word of the new line
                line_cnt = len(word)
        
        #if line still has words left, that is the last line
        if line:
            modline = self.formatLastLine(line, maxWidth)
            res += [modline]
        return res

    def formatLastLine(self, line, maxWidth):
        linestr = " ".join(line)
        linestr += " "*(maxWidth - len(linestr)) #最后补空格
        return linestr

    def formatLine(self, line, line_cnt, maxWidth):
        if len(line) == 1:
            return self.formatLastLine(line, maxWidth)

        linestr = ""
        total_space = len(line) - 1  #此时空格数比单词数少一个
        rest = maxWidth - line_cnt
        spaces, extra = rest // total_space, rest % total_space
        #每个空格处能塞进去的spaces个数, 还有extra的话从左到右再每空格加一个

        for i in range(total_space):  #空格的个数
            extra_str = " " if i < extra else ""
            linestr += line[i] + " " * spaces + extra_str

        linestr += line[-1]
        return linestr


