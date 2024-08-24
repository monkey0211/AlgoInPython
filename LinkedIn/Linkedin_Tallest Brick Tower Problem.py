# Suppose you are trying to build a very tall tower. You have a collection of blocks to make your tower out of. 
# For each block you are given the number of blocks, its weight and the max weight that block can support above it and including itself. 
# Suppose that all blocks have the same height (1 meter), What's the tallest tower you can construct by stacking these blocks? 
# Example input, with each row representing a block type, of format [number _of_blocks, weight, max_support_weight]

# 思路: dp
# dp[i][j]表示使用前i种砖块 总重量为j时的最大高度
# dp[i][j]可以由两种方式转移得来
# 1. dp[i-1][j]:不使用第i块砖
# 2. dp[i-1][j-k*weight[i]] for k:1,2,...count (当前砖可以用1,2,...count块)
# 两者取一个max 就是dp[i][j]
# blocks = [[1, 1, 1], [100, 3, 100], [10, 2, 10]]
# 每一个block分别代表count, weight, tolerance, 计算maxHeight

class Solution: 
    def max_tower_height(self, blocks):
        # 按承重能力（max_support）从小到大排序
        blocks.sort(key=lambda x: x[2])
        
        n = len(blocks)
        #所有blocks累积起来的总重量
        max_weight = sum(block[0] * block[1] for block in blocks)
        
        #初始化dp: 必须需要取到max_weight 所以需要max_weight+1. n代表的是index: 0~n-1
        # dp[blockIndex][weight]: max height if we use index block and have current weights blocks.
        dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            count, weight, max_support = blocks[i-1]
            for j in range(max_weight + 1):
                # 不使用当前砖块
                dp[i][j] = dp[i - 1][j]
                
                # 尝试使用当前砖块
                for k in range(1, count + 1):
                    # 当前重量是j 用了k块重weight的砖 所以之前的状态重量是:(j-k*weight)
                    # 之前的状态必须合法 所以j-k*weight >= 0
                    # 当前的重量必须要在当前砖的承受力之内:j<=max_support 
                    if j >= k * weight and j <= max_support:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - k * weight] + k)
    
    # 返回所有可能总重量中的最大高度
        return max(dp[n])

    # followup: 如果每块砖的高度不一样
    # 还是按照承重能力从小到大排序
    def max_tower_height_w(self, blocks):
        # 按(承重能力递增,高度递减)排序:先用 承重差且高度高的blocks
        blocks.sort(key=lambda x: (x[2], -x[3]))
        
        n = len(blocks)
        max_weight = max(block[2] for block in blocks)
        
        # 初始化dp数组
        dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            count, weight, support, height = blocks[i - 1]
            for w in range(max_weight + 1):
                dp[i][w] = dp[i-1][w]               # 不使用当前块
                
                # 尝试使用当前砖块 枚举可能用多少块当前砖
                for k in range(1, count + 1):
                    if k * weight <= w and w <= support:
                        dp[i][w] = max(dp[i][w], dp[i-1][w - k * weight] + k * height)
        
        return dp[n][max_weight]

# 测试用例
blocks = [[1, 1, 1], [100, 3, 100], [10, 2, 10]]
test = Solution()
print(test.max_tower_height(blocks))

blocksWithWeight = [[1, 1, 1, 2], [100, 3, 100, 1], [10, 2, 10, 3]] 
print(test.max_tower_height_w(blocksWithWeight))