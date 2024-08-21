# Suppose you are trying to build a very tall tower. You have a collection of blocks to make your tower out of. 
# For each block you are given the number of blocks, its weight and the max weight that block can support above it and including itself. 
# Suppose that all blocks have the same height (1 meter), What's the tallest tower you can construct by stacking these blocks? 
# Example input, with each row representing a block type, of format [number _of_blocks, weight, max_support_weight]


# DP: dp[blockIndex][weight]: max height if we have weight blocks and use index block 
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
        dp = [[-1] * (n) for _ in range(max_weight + 1)]
        
        return self.dfs(0, 0, blocks, dp)

    def dfs(self, weight, index, blocks, dp):
        if index == len(blocks):
            return 0
        
        # 如果已经计算过这种情况，直接返回结果
        if dp[weight][index] != -1:
            return dp[weight][index]
        
        # 不使用当前砖块
        res = self.dfs(weight, index + 1, blocks, dp)
        
        count, block_weight, max_support = blocks[index]
        
        # 尝试使用当前砖块
        if weight + block_weight <= max_support:
            for i in range(1, count + 1):
                if weight + i * block_weight > max_support:
                    break
                res = max(res, i + self.dfs(weight + i * block_weight, index + 1, blocks, dp))
        
        dp[weight][index] = res
        return res
# 测试用例
blocks = [[1, 1, 1], [100, 3, 100], [10, 2, 10]]
test = Solution()
print(test.max_tower_height(blocks))