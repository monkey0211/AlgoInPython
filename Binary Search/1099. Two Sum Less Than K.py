class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if not nums: return -1
        nums = sorted(nums)
        res = -1
        left, right = 0, len(nums) - 1
        while left < right:       
            sum = nums[left] + nums[right]
            if nums[left] + nums[right] < k:
                res = max(res, sum)
                left += 1
            else:
                right -= 1
        return res