class Solution:
    # right pointer: scanner, 遇到不为0的就交换
    # 交换完 变成0之后跟着走(+1看下一个)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return 
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0: 
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
   
