# given a nested collection, returning the iteration of the contents of the collections in order. 
# eg. collection = [(1,3,5),(4,7,3),(2,3),4]
# return [1,3,5,4,7,3,2,3,4]

#ref LC341: https://leetcode.com/problems/flatten-nested-list-iterator/
# followup: 增加remove删除当前元素(不是栈顶元素, 此时删除的是上一次 next() 返回的元素)

# 定义一个class Data:
class Data:
    def __init__(self):
        pass
    def isCollection() -> bool:
        pass
    def getCollection():
        pass
    def getElement() -> int:
        pass
    
class DeepIterator:
    # method 1: stack O(n) and O(n)
    def __init__(self, dataList):
        self.stack = []
        for element in reversed(dataList):
            self.stack.append(element)

        self.lastReturned = None # 只在remove时候需要用
        
    def next(self):
        # hasNext确保了栈顶是integer，因此直接弹出栈顶元素
        if self.hasNext():
            return self.stack.pop().getElement()

            # 只在remove时候需要: 需要保存当前弹出的元素
            # self.lastReturned = self.stack.pop()
            # return self.lastReturned.getElement()
        else:
            return None
    
    def hasNext(self):
        #此部分需要放在hasNext. eg. [[]]时候,self.stack.pop().getElement()不可用
        while self.stack and self.stack[-1].isCollection():
            top = self.stack.pop().getCollection()
            for t in reversed(top):
                self.stack.append(t)
        return len(self.stack) > 0
   
    # follow up: implement remove:
    def remove(self):
        # 理解1: 删除next里面pop出来的元素
        # 因为next里面已经pop掉了, 所以这里只是简单地将lastReturned重新标记为None 
        if self.lastReturned:  
            self.lastReturned = None
            
        # 理解2: 删除一个新的元素 不需要lastReturned标记
        if self.hasNext():
            self.stack.pop().getElement()
        else:
            raise Exception("No element to remove or already removed")
        

    # method 2: recursion
    def __init__(self, dataList: [Data]):
        self.flattenedList = [] # 需要用全局list记录(remove的时候需要用)
        self.flatten(dataList)
        self.index = 0 #当前index
    
    def next(self):
        self.index += 1 # 给hasNext做准备
        return self.flattenedList[self.index - 1]
    
    def hasNext(self):
        return self.index < len(self.flattenedList)

    def flatten(self, dataList: [Data]):
        for item in dataList:
            if item.isCollection():
                self.flatten(item.getCollection())
            else:
                self.flattenedList.append(item.getElement())
        return self.flattenedList
    
    # follow up: 删除
    def remove(self):
        if self.index > 0:
            # 删除当前索引之前返回的元素(上一个)
            self.flattenedList.pop(self.index - 1)
            self.index -= 1
        else:
            raise Exception("No element to remove or already removed")

dataList = [[1,1],2,[[]]]
test = DeepIterator(dataList)

print(test.next())
print(test.hasNext())
print(test.remove())