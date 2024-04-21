class MinStack:
  # 需要O(1) getMin, 所以需要两个stack: stack and minStack(每次拿到一个val 把小的放入minStack)
    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1],val))
        
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()