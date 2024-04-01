class Solution:
    # right pointer作为scanner:如果遇到val就继续走, 不是val的时候就nums[i] = nums[j]逐一记录
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i 

        