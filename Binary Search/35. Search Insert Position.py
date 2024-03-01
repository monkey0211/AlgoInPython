from typing import List
class SearchInsert:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        if target <= nums[0]: return 0
        if target > nums[-1]: return len(nums)

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] >= target:
            return left
        else:
            return right
        