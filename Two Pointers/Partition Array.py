from sqlite3 import paramstyle
from typing import List
class Solutions:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] < k: 
                left += 1
            while left < right and nums[right] >= k:
                right -= 1
            if left < right: 
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if nums[left] < k:
            return left + 1
        return left
        print(self.partitionArray([3,2,2,1], 2))

        
        