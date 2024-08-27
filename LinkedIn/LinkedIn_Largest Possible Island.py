# given a 1-dim islandmap, with limited material to convert ocean(0) to island(1),
# find the largest island possible

# sliding window: 每次动right, 把window右端点变为1, cnt+1
# 如果cnt>mateiral数量, 移动左端点, 如果左端点是0, cnt-1
# 更新maxlength
def findLargestIsland(islands, material):
    maxLength = 0
    left = 0
    cnt = 0
    for right in range(len(islands)):    
        if islands[right] == 0:
            cnt += 1
        while cnt > material:
            if islands[left] == 0:
                cnt -= 1
            left += 1
        maxLength = max(maxLength, right - left + 1)
    return maxLength

# followup1: 如果有circle, 把islands延长二倍, 更新maxLength时候有最小值限制
def findLargestIslandWithCircular(islands, material): 
    islands = islands + islands
    maxLength = 0
    left = 0
    cnt = 0
    for right in range(len(islands)):    
        if islands[right] == 0:
            cnt += 1
        while cnt > material:
            if islands[left] == 0:
                cnt -= 1
            left += 1
        maxLength = max(maxLength, min(right - left + 1, len(islands) // 2))
    return maxLength  
    
# followup2: 有obstacle=-1, 每次遇到left指针移动到right前面, reset window cnt.
def findLargestIslandWithObstacles(islands, material):    
    maxLength = 0
    left = 0
    cnt = 0
    for right in range(len(islands)):    
        if islands[right] == 0:
            cnt += 1
        elif islands[right] == -1:
            left = right + 1 # move left to skip over the obstacle
            cnt = 0 # reset
        else:
            while cnt > material:
                if islands[left] == 0:
                    cnt -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
    return maxLength      

# followup3: 有depth 求需要多少material. eg [1, -5, 1], need 6.
def findLargestIslandWithDepth(islands, material):    
    maxLength = 0
    left = 0
    cnt = 0
    maxCnt = 0
    for right in range(len(islands)):    
        if islands[right] <= 0:
            cnt += -islands[right] + 1
        
        while cnt > material:
            if islands[left] <= 0:
                cnt -= 1
            left += 1
        maxLength = max(maxLength, right - left + 1)
   
    return maxLength  
 





islands1 = [0, 1, 0, 1,1,1]
material1 = 1
print(findLargestIsland(islands1, material1))
islands2 = [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1]
material2 = 2
print(findLargestIsland(islands2, material2))
islands4 = [0, 1, 0, 1, 1, 1]
material4= 2
print(findLargestIslandWithCircular(islands4, material4))
islands3 = [0, 1, 0, -1, 1, 1]
material3 = 1
print(findLargestIslandWithObstacles(islands3, material3))
islands5 = [1, -5,0]
material5 = 6
print(findLargestIslandWithDepth(islands5, material5))
