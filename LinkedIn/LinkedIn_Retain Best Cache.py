import heapq

class Rankable:
    def getRank() -> int:
        pass
class DataSource:
    def get(key:K) -> Rankable:
        pass
    
class RetainBestCache:
    def __init__(self, data_source, capacity:int):
        self.data_source = data_source
        self.capacity = capacity
        self.cache = {}
        self.rankHeap = []      
    
    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        
        data = self.data_source[key]
        self.cache.put(key, data)
        heapq.heappush(self.rankHeap, Wrapper(key, data))
        if len(self.rankHeap) > self.capacity:
            wrapper = heapq.heappop(self.rankHeap)
            del self.cache[wrapper.k]
        return wrapper.v 

class Wrapper:
    def __init__(self, k, v):
        self.k = k
        self.v = v
    def __lt__(self, other):
        return self.data.getRank() - other.data.getRank()
    

