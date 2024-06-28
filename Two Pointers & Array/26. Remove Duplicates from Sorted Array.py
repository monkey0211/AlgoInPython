class Solution:
    # right pointer scanning from 1...length, 
    # 遇到和nums[right-1]不相等的就left+1, 数值放入nums[left+1]的空位
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                left += 1
                nums[left] = nums[right]
        print(nums[:left + 1]) #the array after removing duplicate
        return left + 1 