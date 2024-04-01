class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
#需要一个Node class
#需要一个map 存key-> Node(key). #负责用O(1)时间快速拿到需要的key. 
class LRUCache:
    # 对于LRU class 输入只能是key, value

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        # 创建两个dummy, 一个head一个tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.dict = {} 

    def get(self, key: int) -> int:
        if key not in self.dict:          
            return -1
        else:
            node = self.dict[key] 
            self.remove(node)
            self.add(node)         
            return node.value

    def put(self, key: int, value: int) -> None:
        node = Node(key, value) #注意这里的处理 需要先new一个新node
        if key not in self.dict:         
            self.add(node)     
        else:
            prev_node = self.dict[key] # 这里要remove prev_node, add node
            self.remove(prev_node)
            self.add(node)
        
        self.dict[key] = node # anyway都要更新dict
        if len(self.dict) > self.capacity:
            node_to_del = self.head.next
            self.remove(node_to_del) #这里是remove least recency used 就是头节点
            del self.dict[node_to_del.key]
        
    # head -> 0 -> 1 -> tail
    #只需要用到add to tail(this is the dummy tail node)
    def add(self, node):
        tailpre = self.tail.prev
        tailpre.next = node
        node.prev = tailpre
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)