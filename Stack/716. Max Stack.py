import threading


class MaxStack:
    # method 1: O(n) popMax 解法
    # 用两个stack, 一个存当前, 另一个存当前的maxStack, 
    # popMax的时候, maxStack[-1]!=stack[-1]就把上面的这些暂时pop出来存temp, 然后取出相等的那个, 再把temp里面的append回来
    # 记得所有操作, 两个stack都要同步

    def __init__(self):
        self.stack = []
        self.maxStack = []  
        
        # use locks to prevent race conditions:
        # The lock is acquired at the beginning of each method and released at the end, ensuring mutual exclusion
        self.lock = threading.Lock()    
      
    def push(self, x: int) -> None:
        with self.lock: # add if needed
            self.stack.append(x)
            if not self.maxStack:
                self.maxStack.append(x)
            else:
                self.maxStack.append(max(self.maxStack[-1], x))
        
    def pop(self) -> int:
        with self.lock: # add if needed
            top = self.stack.pop()
            self.maxStack.pop()
            return top
    
    def top(self) -> int:
        # with self.lock:  # add if needed
        return self.stack[-1]
        
    def peekMax(self) -> int:
        # with self.lock:  # add if needed
        return self.maxStack[-1]

    def popMax(self) -> int: 
        # with self.lock:  # add if needed
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


    # method 2: doublelinkedlinst(作为stack) + maxHeap + defaultdict(list)
import collections
import heapq
class DoubleLinkedList:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.pre = None
	
class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.stack = DoubleLinkedList(float('-inf')) # init a dummy node
        self.last = self.stack                       # reference the stack tail
        self.heap = []
        self.dict = collections.defaultdict(list)
        

    def push(self, x: int) -> None:
        # O(logn)
        node = DoubleLinkedList(x)
        
        # update the tail
        self.last.next = node
        node.pre = self.last
        self.last = node
        
        # push -x to the heap(max)
        heapq.heappush(self.heap, -x)
        
        # append node the the map entry
        self.dict[x].append(node)
        
    def pop(self) -> int:
        # O(1)
        # pop from the stack and remove from map
        num = self.last.val
        self.last = self.last.pre
        self.last.next = None
        
        self.dict[num].pop()
        if not self.dict[num]:
            del self.dict[num]
        return num

    def top(self) -> int:
        # O(1)
        return self.last.val

    def peekMax(self) -> int:
        # O(logN)
        # during the pop(), we didn't remove the element from heap
        # So here is to remove the the poped elements from heap
        while -self.heap[0] not in self.dict:
            heapq.heappop(self.heap)
        
        return -self.heap[0]

    def popMax(self) -> int:
        # O(logN) 因为peekMax是logN
       
        num = self.peekMax() #get max
        node = self.dict[num].pop()   # pop from map
        if not self.dict[num]: #可能有多个duplicate, 所以hmap可能没有了
            del self.dict[num]
        
        # 如果pop的是tail: update the tail reference
        if node == self.last:
            self.last = self.last.pre
        
        # remove the node from stack(double linkedlist)
        if node.pre:
            node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre
        return num