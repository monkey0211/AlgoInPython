class Solution:
    # 区别46: input has duplicate, output不能重复取: eg. [1(1), 1(2), 2]和[1(2), 1(1), 2]是一样的 不能取两个
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        tmp = []
        visited = set()
        self.dfs(nums, res, tmp, visited)
        return res
    
    def dfs(self, nums, res, tmp, visited):
        if len(tmp) == len(nums):
            res.append(tmp[:])
            return
        
        for i in range(len(nums)):
            #多加一个限制: 前面数用过 就不能再用.eg. [1(1), 1(2), 2]和[1(2), 1(1), 2]是一样的 不能取两个
            if i != 0 and nums[i] == nums[i - 1] and i-1 not in visited:
                continue
            if i not in visited:           
                tmp.append(nums[i])
                visited.add(i)
                self.dfs(nums, res, tmp, visited)
                visited.remove(i)
                tmp.pop()
                