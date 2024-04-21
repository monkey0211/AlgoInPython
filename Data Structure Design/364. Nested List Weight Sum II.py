# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList: return 0
        queue = collections.deque(nestedList)
        res = [] # append记录每层的subtotal, or use stack(pop to calculate each element)

        while queue:
            subtotal = 0
            
            for i in range(len(queue)):
                item = queue.popleft()
                if item.isInteger():
                    subtotal += item.getInteger()
                else:
                    queue.extend(item.getList())
            res.append(subtotal)
        
        total = 0
        maxDepth = len(res)
        for i in range(len(res)):
            total += (maxDepth - i)*res[i]
        return total
            
