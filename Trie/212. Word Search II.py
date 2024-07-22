class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None #to store最后形成的word

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self,word):
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if not child:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True
        node.word = word

class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.add(word)
        
        res = set()
        visited = set()

        ##遍历字母矩阵，将每个字母作为单词首字母开始搜索
        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                visited.add((i, j))
                self.dfs(board, i, j, res, visited, trie.root.children.get(char))
                visited.remove((i, j))
        return list(res)
    
    def dfs(self, board, x, y, res, visited, node):
        if not node:
            return
        
        if node.isWord == True:
            res.add(node.word) #这里不能直接return 因为可能没有搜完 下面还会有
        
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for k in range(4):
            newx = x + dx[k]
            newy = y + dy[k]
            if 0 <= newx < len(board) and 0 <= newy < len(board[0]) and (newx, newy) not in visited:
                visited.add((newx, newy))
                newchar = board[newx][newy]
                self.dfs(board, newx, newy, res, visited, node.children.get(newchar))
                visited.remove((newx, newy))

        
            
