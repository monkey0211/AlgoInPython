class Solution:
# greedy:  tc O(n) sc O(1) 求min steps he can go.**
# maxReach:record the furthest distance he can go.
# end is the boarder: need to update boarder when i(pointer) meet end. then step +1
    def jump(self, nums: List[int]) -> int:
        if not nums: return 0
        maxReach = 0
        end, step = 0, 0

        for i in range(len(nums)-1):
            if i <= maxReach:
                maxReach = max(maxReach, nums[i]+i)
                if i == end:
                    end = maxReach
                    step+= 1
        return step
