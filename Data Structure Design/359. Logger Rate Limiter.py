class Logger:
# method 1: hashmap. dict[message] = timestamp
# (but if too many messages, consume too many memory)
    def __init__(self):
        self.dict = {} # 用dict记录message->last timestamp   

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if not self.dict or message not in self.dict:
            self.dict[message] = timestamp
            return True
        else:
            if timestamp - self.dict[message]<10: 
                return False
            else:    
                self.dict[message] = timestamp
                return True

# method 2: queue + set.  time O(n) space O(n)
# queue: 存10s内的(ts, msg). 10s之内任何message只有一次. pop all elements that > 10 and remove in set.
# set: 记录在queue里的msg. queue里如果pop set也需要remove

    def __init__(self):
        self.queue = collections.deque()
        self.set = set()


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        while self.queue and timestamp - self.queue[0][0] >= 10:
            ts, msg = self.queue.popleft()
            self.set.remove(msg)

        if message not in self.set:
            self.queue.append((timestamp, message))
            self.set.add(message)
            return True
        else:
            return False


        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)