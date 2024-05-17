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
    # method 1: BFS level order traversal. 
    # ref related LC341: https://leetcode.com/problems/flatten-nested-list-iterator/description/
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        level = 0
        total = 0
        queue = collections.deque(nestedList) #要把整个nestedList放进去, 因为不是level traversal 是全部遍历 带int的为第一层.
        
        while queue:
            level += 1
            for i in range(len(queue)):
                n = queue.popleft()
                if n.isInteger():
                    total += n.getInteger()*level
                else:
                    queue.extend(n.getList()) #打开list取出来 放入queue 这样下一轮会看到list里面的元素
        return total
        