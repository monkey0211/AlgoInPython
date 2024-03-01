class Solution:
    # 找到所有a+b = -c的unique pair. input may have duplicate->output unique
    # Two Pointers: Time O(n^2) time,  Space o(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []

        self.res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            # skip duplicate triples with the same first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1 #不回头 所以只需要[i+1, right]这一段
            self.findTwoSumPair(left, right, nums, target)
    
        return self.res
    
    def findTwoSumPair(self, left, right, nums, target):
        triple = []
        while left < right:
            if nums[left] + nums[right] == target:
                triple = [nums[left], nums[right], -target]
                self.res.append(triple) #here to update final results
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
           
            elif left < right and nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
            