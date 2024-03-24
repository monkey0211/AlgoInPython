class Solution:
    # input: duplicates are allowed. output: no duplicate is allowed.
    # need sort(目的是把相同的放一起) 判断nums[i] == nums[i-1]
    # time O(n*2^n) space O(n) for sort
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:return []
        nums = sorted(nums) #必须要sort 为了把相同元素放一起 
        res = []
        temp = []
        self.dfs(temp, res, nums, 0)
        return res
    
    def dfs(self, temp, res, nums, index):
        res.append(temp[:])

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:  #注意这里头元素是index
                continue
            temp.append(nums[i])
            self.dfs(temp, res, nums, i + 1)
            temp.pop()
        