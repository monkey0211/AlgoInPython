class TrieNode:
    def __init__(self, val = 0):
        self.val = val
        self.children = {}
        self.prodList = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prodList.append(word) # 对每个位置的node都用prodList记录当前的list
            print(node, node.prodList)
            node.prodList.sort()
            if len(node.prodList) > 3:
                node.prodList.pop()

    def search(self, word): # search for 以char结尾位置的所有product list
        node = self.root
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.prodList

class Solution:
    #build trie. 
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        # create the trie
        for p in products:
            trie.insert(p)
        
        res = []
  
        for i in range(len(searchWord)):
            prefixWord = trie.search(searchWord[:i+1])
            res.append(prefixWord)
        return res