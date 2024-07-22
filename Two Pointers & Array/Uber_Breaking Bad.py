#  Uber: https://leetcode.com/discuss/interview-experience/2008790/uber-phone-screen
# You're given a set of symbols for the elements in the periodic table [.... Li, Be, B, C, N, F, Ne, Na, Co, Ni, Cu, Ga, Al, Si.....]

# Write the function breakingBad(name, symbols) that given a name and a set of symbols returns the phrase with the following format [Symbol]rest of the word

# Example:
# symbols = [H, He, Li, Be, B, C, N, F, Ne, Na, Co, Ni, Cu, Ga, Al, Si, Fa]
# breakingBad("henry alba", symbols) results in [He]nry [Al]ba

# Follow up: we only care about the longest symbol within a word. Example in the word henry there are two elements that are present [H] & [He] and we want He in the output phrase and not H.

# 用trie(可以节省空间) 建立字典 注意大小写
class TrieNode:
    def __init__(self, ch = ""):
        self.ch = ch
        self.children = {}
        self.is_end_of_symbol = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, symbol):
        node = self.root
        for char in symbol:
            lower_char = char.lower()
            if lower_char not in node.children:
                node.children[lower_char] = TrieNode(char) #children的key是小写, ch值是原始char
            node = node.children[lower_char]
           
        node.is_end_of_symbol = True
    
    def search_longest_symbol(self, word: str): #此处的word is lower. 
        longest_symbol = ""
        node = self.root
        current_symbol = ""
        for _, char in enumerate(word):
            if char in node.children:
                node = node.children[char]
                current_symbol += node.ch #这里需要的是原始值
                print(current_symbol)
                if node.is_end_of_symbol:
                    longest_symbol = current_symbol
            else:
                break
        
        return longest_symbol
class Solution:
    def breakingBad(self, name, symbols):
        trie = Trie()
        for symbol in symbols:
            trie.insert(symbol)
        
        words = name.split()
        result = []
        
        for word in words:
            longest_symbol = trie.search_longest_symbol(word.lower())
            print("ls:", longest_symbol)
            
            if longest_symbol:
                start_index = word.lower().index(longest_symbol.lower()) #这里是lower, 用index
                end_index = start_index + len(longest_symbol)
                formatted_word = word[:start_index] + "[" + longest_symbol + "]" + word[end_index:]
                result.append(formatted_word)
            else:
                result.append(word)
        
        return ' '.join(result)

# Example usage
test = Solution()
symbols = ["H", "He", "Li", "Be", "B", "C", "N", "F", "Ne", "Na", "Co", "Ni", "Cu", "Ga", "Al", "Si", "Fa"]
name = "henry alba"
print(test.breakingBad(name, symbols))


 
