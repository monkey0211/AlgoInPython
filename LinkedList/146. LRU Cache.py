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
        newnode = Node(key, value) #注意这里的处理 需要先new一个新node
        if key in self.dict: # 这里要remove oldnode, add newnode
            oldnode = self.dict[key]
            self.remove(oldnode)
            self.add(newnode)
            self.dict[key] = newnode
        else:
            self.add(newnode) #每次的add/remove dict里面都要一起
            self.dict[key] = newnode
            if len(self.dict) > self.capacity:
                toRemove = self.head.next
                self.remove(toRemove)
                del self.dict[toRemove.key]    
        
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