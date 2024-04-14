class Solution:
    # 在i <= maxReach情况下不断更新maxReach. 如maxReach >= lenth - 1说明可以都走完 返回True
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        maxReach = nums[0]

        for i in range(1, len(nums)):
            if i <= maxReach:
                maxReach = max(maxReach, nums[i]+i)
        if len(nums)-1 <= maxReach: 
            return True
        