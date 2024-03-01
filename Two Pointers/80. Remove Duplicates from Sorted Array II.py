class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2: return len(nums)
        i = 1
        cnt = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                cnt = 1
            else:
                cnt += 1
            # For a count <= 2, we copy the element thus
            # overwriting the element at index "i" in the array
            if cnt <= 2:
                nums[i] = nums[j]
                i += 1 #i跳到下一个空位

        return i 
