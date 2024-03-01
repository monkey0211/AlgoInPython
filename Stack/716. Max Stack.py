class MaxStack:
    # O(n) popMax 解法
    # 用两个stack, 一个存当前, 另一个存当前的maxStack, 
    # popMax的时候, maxStack[-1]!=stack[-1]就把上面的这些暂时pop出来存temp, 然后取出相等的那个, 再把temp里面的append回来
    # 记得所有操作, 两个stack都要同步

    def __init__(self):
        self.stack = []
        self.maxStack = []     

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.maxStack:
            self.maxStack.append(x)
        else:
            self.maxStack.append(max(self.maxStack[-1], x))
    
    def pop(self) -> int:
        top = self.stack.pop()
        self.maxStack.pop()
        return top
    def top(self) -> int:
        return self.stack[-1]
        
    def peekMax(self) -> int:
        return self.maxStack[-1]

    def popMax(self) -> int: 
        temp = []
        while self.maxStack[-1] != self.stack[-1]:
            temp.append(self.pop())
      
        result = self.pop()
     
        while temp:
            self.push(temp.pop()) #两个stack必须都要加回来    
        return result
        

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()