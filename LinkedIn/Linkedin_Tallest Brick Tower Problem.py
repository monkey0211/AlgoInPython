# DP
# dp[weight][blockIndex]: max height if we have weight blocks and use index block 
def tallest_tower(blocks):
    height = 0
    
    table = []
    for i in range(maxTolerance + 1):
        table.append([])
        
    