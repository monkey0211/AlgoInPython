from typing import List
class Search:
    # assumption: no duplicate
    # followup: if single transpose/rotation or multiple, it is the same, no difference
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right: 
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] > nums[right]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

test = Search()
print(test.search([1,1,1,2,0,1], 2))