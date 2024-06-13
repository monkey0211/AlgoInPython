class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, paths, val): #传入的是一个需要拆分做成trie的list
        node = self.root
        for i in range(len(paths)):
            if paths[i] not in node.children: # Parent path does NOT exist
                if i != len(paths) - 1: #只有i是最后一个才可以insert: 此时创建新node
                    return False 
                node.children[paths[i]] = TrieNode()
            node = node.children[paths[i]] #此时node指向的是当前位置
        if node.val:
            return False
        node.val = val
        return True
    
    def search(self, paths):
        node = self.root
        for p in paths:
            if p not in node.children:
                return -1
            node = node.children[p]
        return node.val if node.val else -1


class FileSystem:

    def __init__(self):
        self.trie = Trie()
        

    def createPath(self, path: str, value: int) -> bool:
        paths = path[1:].split("/")
        return self.trie.insert(paths, value)
        

    def get(self, path: str) -> int:
        paths = path[1:].split("/")
        return self.trie.search(paths)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)