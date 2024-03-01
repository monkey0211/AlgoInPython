class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x: int) -> None:
        
        self.q1.append(x)

    def pop(self) -> int:
        # 如果q1为空 switch q1 and q2, 说明需要pop之前的element都已经在q2, 换回到q1
        # 需要pop最后一个元素, 把之前的所有都放入q2, 然后取出剩下的top one. 
        # can use only one queue: just append all previous elements to end of q1 again.
        
        if not self.q1: 
            self.q1, self.q2 = self.q2, self.q1
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        return self.q1.popleft()
        

    def top(self) -> int:
        if not self.q1: 
            self.q1, self.q2 = self.q2, self.q1
        if self.q1:
            return self.q1[-1]
        

    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()