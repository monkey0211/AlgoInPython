class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        nums = [lower-1] + nums + [upper+1] # way of making a new nums
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                res.append((nums[i-1 ]+ 1, nums[i] - 1))      
        return res
        
    #   meta变形: 
    #       res.append(self.getString(nums[i-1 ]+ 1, nums[i] - 1))
    # def getString(self, n1, n2):
    #     if n1 == n2:
    #         return str(n1)
    #     else:
    #         return str(n1) + "->" + str(n2)