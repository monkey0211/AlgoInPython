class Solution:
# nums不是在increasing就是在decreasing 不需要一直严格单调 
# 但是不会有平的情况(相邻元素不相等) maybe multiple peaks
# 数组的两个边界外侧 可以认为值是负无穷
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
    
    # aaron version
    def findPeakElement_v1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # mid+1不会越界 如果mid+1越界 说明mid==len 说明l==r==len 但l==r不会进入循环 矛盾
            if nums[mid] > nums[mid + 1]: # mid可能是答案
                right = mid
            else:                        # mid一定不是答案
                left = mid + 1
        return right