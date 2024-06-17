import collections

class Solutions:
    def getClosestCities(self, cities, xValues, yValues, queries):
        citymap = {}
        res = []
        for i in range(len(cities)):
            citymap[cities[i]] = i
        
        for query in queries:
            if query not in citymap:
                continue
            print(query)
            index = citymap[query] # get the query index and query x, y
            cityIndex = self.closestCity(cities, xValues, yValues, index)
            res.append(cities[cityIndex])
        return res 
    
    def closestCity(self, cities, x, y, index):
        res = -1
        minDist = float("inf")
        x, y = xValues[index], yValues[index]
        for i in range(len(cities)):
            if i != index:
                if xValues[i] == x or yValues[i] == y:
                    dist = abs(xValues[i] - x) + abs(yValues[i] - y)
                    if dist < minDist:
                        minDist = dist
                        res = i
                    elif dist == minDist:
                        if cities[i]<cities[res]:
                            res = i
        return res

    # def compareTo(self, lhs, rhs)->int:
    #     if lhs < rhs: 
        
test = Solutions()
cities = ["axx", "axy", "az", "axd", "aa", "abc", "abs", "p"]
xValues = [0,1,2,4,5,0,1,0]
yValues = [1,2,5,3,4,2,0,2]
queries = ["axx", "axy", "abs", "zmm"]
print(test.getClosestCities(cities, xValues, yValues, queries))