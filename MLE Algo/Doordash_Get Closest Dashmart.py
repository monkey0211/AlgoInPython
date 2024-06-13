import collections

class Solutions:
# doordash: 
    def getClosestDashmart(self, city, locations):
        res = []
        queue = collections.deque()
        for i in range(len(city)):
            for j in range(len(city[0])):
                
                if city[i][j] == "D":
                    city[i][j] = "0"
                    queue.append((i, j))
        while queue:
            x, y = queue.popleft()

            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            for d in range(4):
                newx = dx[d] + x
                newy = dy[d] + y
                if 0 <= newx < len(city) and 0 <= newy < len(city[0]) and city[newx][newy] == " ":
                    city[newx][newy] = str(int(city[x][y]) + 1)
                    queue.append((newx, newy))
                  
       
        for x, y in locations:
            res.append(int(city[x][y]))
            
        return res     

# Asked as a follow-up - What if we can traverse X except the ones which is surrounded by Xs at all 4 directions? What would be the solution?
# answer: Traverse and mark as "Y"
city = [
 ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'], # 0
 ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'], # 1
 [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '], # 2
 [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '], # 3
 [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'], # 4
 [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X'] # 5
 ]

locations = [
 [2, 2],
 [4, 0],
 [0, 4],
 [2, 6],
]
test = Solutions()
print(test.getClosestDashmart(city, locations))