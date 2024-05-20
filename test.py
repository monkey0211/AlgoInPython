import collections
class Test:
    def shortestPathBinaryMatrix(self, intervals):
        res = []
        for x, y in intervals:
            if not res:
                res.append([x, y])
            elif res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(res[-1][1], y)
        return res
    
test = Test()
print(test.shortestPathBinaryMatrix([[1,4],[4,5]]))
    