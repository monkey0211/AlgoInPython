# return the smallest character that is strictly larger than the serach cahracter
# if none found, return the first element of the array(wrap around)

R = ["c", "f", "j", "p", "v"]

def findInsPoint(R, char):
    if char >= R[-1] or char < R[0]: #注意第一个和最后一个元素
        return R[0]
    left, right = 0, len(R) - 1
    while left + 1 < right:
        mid = (left + right) // 2 # (right-left)//2+left
        if R[mid] <= char:
            left = mid
        else:
            right = mid 
    
    if R[left] > char:
        return R[left] 
    else:
        return R[right] 

print(findInsPoint(R, "a"))
    
# follow up:
# what if range were expanded beyond letters? case sensitivity
# application: partition schema  
# if duplicate? 也可以.(区别如果是找local min, worst o(n))

        
    