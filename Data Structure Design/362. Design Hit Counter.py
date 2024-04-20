class HitCounter:
    # 需要用deque

    def __init__(self):
        self.queue = collections.deque()
        
    def hit(self, timestamp: int) -> None:
        if not self.queue:
            self.queue.append(timestamp)
        else:
            if timestamp - self.queue[0]< 300:
                self.queue.append(timestamp)
            else:
                self.queue.popleft()
                self.queue.append(timestamp)      

    def getHits(self, timestamp: int) -> int:
        cnt = 0
        for t in self.queue:
            if timestamp - t < 300:          
                cnt += 1
                print(t, timestamp, cnt, self.queue)
         
        return cnt