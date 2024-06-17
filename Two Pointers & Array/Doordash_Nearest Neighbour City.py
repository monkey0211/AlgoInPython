import collections
# Doordash: Nearest Neighbour City. 
# ref: LC1779: https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

# A number of cities are arranged on a graph that has been divided up like an ordinary Cartesian plane. 
# Each city is located at an integral (x, y) coordinate intersection. City names and locations are given in the form of three arrays: c, x, and y, 
# which are aligned by the index to provide the city name (c[i]), and its coordinates, (x[i], y[i]). 
# Determine the name of the nearest city that shares either an x or a y coordinate with the queried city. 
# If no other cities share an x or y coordinate, return 'NONE'. If two cities have the same distance to the queried city, q[i], consider the one with an alphabetically shorter name (i.e. 'ab' < 'aba' < 'abb') as the closest choice. 
# The distance is the Manhattan distance, the absolute difference in x plus the absolute difference in y.
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
        
test = Solutions()
cities = ["axx", "axy", "az", "axd", "aa", "abc", "abs", "p"]
xValues = [0,1,2,4,5,0,1,0]
yValues = [1,2,5,3,4,2,0,2]
queries = ["axx", "axy", "abs", "zmm"]
print(test.getClosestCities(cities, xValues, yValues, queries))