class Solution:
    # input: no duplicates
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []
        temp = []
        self.dfs(res, temp, 0, nums)
        return res
    
    def dfs(self, res, temp, index, nums):
        res.append(temp[:])

        for i in range(index, len(nums)): #头元素从index开始
            temp.append(nums[i])
            self.dfs(res, temp, i + 1, nums)
            temp.pop()
        