class AllOne:
#构建DLL: Node(0:{}) <-> Node(1:{hello}) -- Node(1:{hi, bags}) .....
    # bucket of counts [(index, [list of vals])]
    # map of key: index
    def __init__(self):
        self.bucket = DoubleLinkedList()
        self.dict = {} # map keys to nodes

    def inc(self, key: str) -> None:
        node = self.bucket.head if key not in self.dict else self.dict[key] # 如果不在dict里就是DLL的head
        new_node = self.bucket.incrementElement(node, key)
        self.dict[key] = new_node

    def dec(self, key: str) -> None:
        node = self.dict[key]
        new_node = self.bucket.decrementElement(node, key)
        if new_node.index == 0:
            new_node.removeElement(key)
            del self.dict[key]
        else:
            self.dict[key] = new_node

    # DLL的tail.prev
    def getMaxKey(self) -> str:
        max_node = self.bucket.tail.prev
        if max_node.index == 0:
            return ""
        for e in max_node.keys:
            return e

    # DLL的head.next
    def getMinKey(self) -> str:
        min_node = self.bucket.head.next
        if min_node.index < float("inf"):
            for e in min_node.keys:
                return e
        else:
            return ""
    
class DoubleLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(float("inf"))
        self.head.next = self.tail
        self.tail.prev = self.head

    def decrementElement(self, node, key):
        node.removeElement(key)
        prevNode = node.prev
        correctNode = None
        if prevNode.index == node.index - 1:
            # Node(index-1)已经存在, 直接插入
            correctNode = prevNode
        else:
            # insert new node
            correctNode = self.insertNext(prevNode, node.index - 1)
        
        if not node.keys:
            self.pop(node)

        correctNode.addElement(key)
        return correctNode

    def incrementElement(self, node, key):
        if node.index != 0:
            node.removeElement(key)
        correctNode = None
        if node.next.index == node.index + 1: #该node的下一个node存在
            correctNode = node.next
        else: #如果不存在, 创建一个新的node(index+1) 插入该位置
            correctNode = self.insertNext(node, node.index + 1)

        correctNode.addElement(key)
        if not node.keys:
            self.pop(node)
        
        return correctNode

    # insert a node after this node with index+1
    def insertNext(self, node, index):
     
        nextNode = node.next
        new_node = Node(index)

        new_node.prev = node
        new_node.next = nextNode
        node.next = new_node
        nextNode.prev = new_node

        return new_node

    # pop the node if it has no keys
    def pop(self, node):
        
        if node.index == 0 or node.index == float("inf"):
            return
        #重新连接两个node
        prev = node.prev
        nextNode = node.next
        prev.next = nextNode
        nextNode.prev = prev
        return

class Node:
    def __init__(self, index):
        self.keys = set()
        self.index = index # node的value/index
        self.prev = None
        self.next = None

    def removeElement(self, key):
        self.keys.remove(key)

    def addElement(self, key):
        self.keys.add(key)