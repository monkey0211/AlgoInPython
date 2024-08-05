class Solution:
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
            if i != 0 and nums[i] == nums[i - 1] and i-1 not in visited:
                continue
            if i not in visited:           
                tmp.append(nums[i])
                visited.add(i)
                self.dfs(nums, res, tmp, visited)
                visited.remove(i)
                tmp.pop()
                