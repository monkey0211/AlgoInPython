class Solution:
    #二分: 用missingCount(index)表示index之前missing的数量, 最后只需要return left在的missingCount
    def missingElement(self, nums: List[int], k: int) -> int:
   
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if self.missingCount(mid, nums) >= k:
                right = mid
            else:
                left = mid
        #最后无论如何都是返回left的值, 如果不缺, 就return right+k+nums[0]也就是left+1
        if self.missingCount(left, nums) >= k:
            return left + k + nums[0]
        elif self.missingCount(right, nums) >= k:
            return left + k + nums[0]
        else:
            return right + k + nums[0]
    
    def missingCount(self, index, nums):
        return nums[index] - nums[0] - index

        