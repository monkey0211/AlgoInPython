import collections
# Meta 986 or 56变形题(取union not intersection): https://leetcode.com/discuss/interview-question/124616/
class Solutions:
    # two pointer 1)find the smaller one, assign to curr. 
    # 然后类似merge interval:比较res[-1]和curr, 看是否需要append
    def mergeTwoIntervalList(self, firstList, secondList):
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]
            if first[0] < second[0]:
                curr = first
                i += 1
            else:
                curr = second
                j += 1
            self.mergeIntervals(curr, res)
            print(curr, res)
        
        while i < len(firstList):
            curr = firstList[i]
            self.mergeIntervals(curr, res)
            i += 1
        while j < len(secondList):
            curr = secondList[j]
            self.mergeIntervals(curr, res)
            j += 1      
        return res 
    
    def mergeIntervals(self, curr, res):
        if not res or res[-1][1] < curr[0]:
            res.append(curr)
        else:
            res[-1][1] = max(res[-1][1], curr[1])

            
A = [[1,5],[10,14],[16,18]]
B = [[2,6],[8,10],[11,20]]
test = MergeTwoIntervalList()
print(test.mergeTwoIntervalList(A, B))