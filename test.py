class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word_sequence = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word_sequence):
        node = self.root
        for word in word_sequence:
            if word not in node.children:
                node.children[word] = TrieNode()
            node = node.children[word]
        node.is_end_of_word = True
        node.word_sequence = word_sequence  # 记录完整单词序列
    
    def search_longest_match(self, words, start_index):
        node = self.root
        longest_match = None
        i = start_index
        
        while i < len(words) and words[i] in node.children:
            node = node.children[words[i]]
            if node.is_end_of_word:
                longest_match = node.word_sequence
            i += 1
        
        return longest_match

def tag_usernames(input_text, user_names):
    # 构建 Trie 树
    trie = Trie()
    for name in user_names:
        trie.insert(name.split())
    
    words = input_text.split()
    i = 0
    result = []
    while i < len(words):
        match = trie.search_longest_match(words, i)
        if match:
            result.append("@" + " ".join(match))
            i += len(match)  # 跳过匹配的单词
        else:
            result.append(words[i])
            i += 1
    
    return ' '.join(result)

# 示例输入
input_text = "Lucy Wang has an interview with John Chen"
user_names = ["Lucy", "Wang", "Lucy Wang", "John", "Chen", "John Chen"]

# 调用函数并输出结果
output_text = tag_usernames(input_text, user_names)
print(output_text)
