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
    
    # Gets some data. 
	#  * If possible, retrieves it from cache to be fast. If the data is not cached, 
	#  * retrieves it from the data source. If the cache is full, attempt to cache the returned data, 
	#  * evicting the T with lowest rank among the ones that it has available 
	#  * If there is a tie, the cache may choose any T with lowest rank to evict. 
	#  * 
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

# 

