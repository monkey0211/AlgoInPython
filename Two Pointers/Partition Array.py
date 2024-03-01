from typing import List
class Solutions:
    #此题返回的是数组划分位置(k所在的index).
    # return how many numbers < k
    # 注意: 1. 推出条件需要一致 2.分别找出左边第一个不满足条件的和第一个右边不满足条件的(注意取等)
    def partitionArray(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k: 
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right: 
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return left

        
        