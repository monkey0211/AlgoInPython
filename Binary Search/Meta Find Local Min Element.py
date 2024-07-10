#ref: https://leetcode.com/problems/find-peak-element/description/
#二分, 严格递增情况 无相等元素
class Solution: 
    def findMinElement(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                right = mid
            else:
                left = mid
        
        if nums[left] < nums[right]:
            return left
        else:
            return right
test = Solution()
nums = [1,2,3, 1]
print(test.findMinElement(nums))