class Solution:
    # input: no duplicate
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
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
            # 除去自己的方法两种: 
            # 1. if nums[i] not in visited: continue 
            # 2. if nums[i] not in temp: continue
            if nums[i] not in visited:
                visited.add(nums[i])
                tmp.append(nums[i])
                self.dfs(nums, res, tmp, visited)
                tmp.pop()
                visited.remove(nums[i])

        