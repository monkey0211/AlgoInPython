class Solution:
# array需要strictly increasing/decreasing, + maybe multiple peaks
# target为相邻元素 如果nums[mid]和nums[mid+1] 取大的一边
# 否则取大的一边，两个都大，可以随便取一边。最终会找到peak
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid
        if nums[left] < nums[right]:
            return right
        else:
            return left 