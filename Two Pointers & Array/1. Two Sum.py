class Solution:
    # hashmap: 必须保证: no duplicate in nums. Time: O(n), space o(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums: return [-1, -1]
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [i, dict[target - nums[i]]]
            
    
        
        