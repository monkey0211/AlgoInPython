# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    
    # method 1: stack O(n) and O(n)
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for element in reversed(nestedList):
            self.stack.append(element)

        self.last_returned = None # 只在remove时候需要用
        
    def next(self) -> int:
        # 只在remove时候需要: hasNext 确保了栈顶是整数，因此直接弹出栈顶元素
        # if self.hasNext():
        #     self.last_returned = self.stack.pop()
        #     return self.last_returned.getInteger()
        
        # 如果直接是一个integer 直接取出
        return self.stack.pop().getInteger()
        
    def hasNext(self) -> bool:
        #此部分需要放在hasNext. eg. [[]]时候,self.stack.pop().getInteger()不可用
        while self.stack and not self.stack[-1].isInteger():
            top = self.stack.pop().getList()
            for t in reversed(top):
                self.stack.append(t)
        return len(self.stack) > 0
    # follow up: implement remove:
    def remove(self):
        if self.last_returned is not None:
            # 这里只是简单地将 last_returned 标记为 None 表示已经被移除
            self.last_returned = None
        else:
            raise Exception("No element to remove or already removed")
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

    # method 2: recursion
    def __init__(self, nestedList: [NestedInteger]):
        self.flattenedList = [] # 需要用全局list记录(remove的时候需要用)
        self.flatten(nestedList)
        self.index = 0
    
    def next(self):
        self.index += 1
        return self.flattenedList[self.index - 1]
    
    def hasNext(self):
        return self.index < len(self.flattenedList)

    def flatten(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.flattenedList.append(item.getInteger())
            else:
                self.flatten(item.getList())
        return self.flattenedList
    
    # follow up: 删除
    def remove(self):
        if self.index > 0:
            # 删除当前索引之前返回的元素
            self.flattenedList.pop(self.index - 1)
            self.index -= 1
        else:
            raise Exception("No element to remove or already removed")